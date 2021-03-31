from sqlalchemy.orm import Session, lazyload

from models import City, Forecast
from schemas import (
    CityEntity, CityCreate, ForecastBase)


def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).options(
        lazyload(City.forecasts)).first()


def get_city_by_name(db: Session, city_name: str):
    return db.query(City).filter(City.name == city_name).options(
        lazyload(City.forecasts)).first()


def get_forecast_by_date(db: Session, city_id: int, date: int):
    return db.query(Forecast).filter(
        Forecast.city_id == city_id, Forecast.date == date).first()


def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(City).offset(skip).limit(limit).all()


def get_or_create_city(db: Session, city: CityCreate):
    city_exists = get_city_by_name(db, city.name)
    if city_exists:
        return city_exists

    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def create_forecast(db: Session, forecast: dict, city_id: int):
    db_forecast = Forecast(**forecast.dict(), city_id=city_id)
    db.add(db_forecast)
    db.commit()
    db.refresh(db_forecast)
    return db_forecast
