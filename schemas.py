from typing import List, Optional

from pydantic import BaseModel


class ForecastBase(BaseModel):
    date: int
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float
    main: str
    description: str


class ForecastCreate(ForecastBase):
    pass


class ForecastEntity(ForecastBase):
    id: int
    city_id: int

    class Config:
        orm_mode = True


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class CityEntity(CityBase):
    id: int
    forecasts: List[ForecastEntity] = []

    class Config:
        orm_mode = True


