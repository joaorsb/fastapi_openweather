import json
import os

from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from services import get_open_weather_forecast
from schemas import CityEntity, CityCreate, ForecastEntity, ForecastCreate
from models import Base
from database import SessionLocal, engine
from db_manager import (
    get_or_create_city,
    get_forecast_by_date,
    create_forecast,
    get_city_by_name,
    get_cities, get_city)

Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[CityEntity])
async def get_city_forecast(
    db: Session = Depends(get_db)
):
    cities = get_cities(db)
    return cities


@router.get("/search", response_model=CityEntity)
async def get_city_forecast(
    city: str = Query(None), db: Session = Depends(get_db)
):
    if not city:
        raise HTTPException(418, detail="City not given")

    api_key = os.environ.get('OPEN_WEATHER_API_KEY')
    metric = 'metric'
    open_weather_url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={city},BR&units={metric}&cnt=5&appid={api_key}"
    forecast_json_response = await get_open_weather_forecast(open_weather_url)
    forecast_response = json.loads(forecast_json_response)
    try:
        list_forecasts = forecast_response['list']
        city_name = forecast_response['city']['name']
        city_entity = CityCreate(name=city_name)
        city_model = get_or_create_city(db, city_entity)

        for item in list_forecasts:
            temp = item['temp']
            forecast = get_forecast_by_date(db, city_model.id, item['dt'])
            if not forecast:
                forecast_entity = ForecastCreate(
                    date=item['dt'],
                    day=temp['day'],
                    min=temp['min'],
                    max=temp['max'],
                    night=temp['night'],
                    eve=temp['eve'],
                    morn=temp['morn'],
                    main=item['weather'][0]['main'],
                    description=item['weather'][0]['description'],
                )
                _ = create_forecast(db, forecast_entity, city_model.id)
    except IndexError:
        HTTPException(404, detail=f"Forecast not found for city: {city}")

    return city_model
