from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    forecasts = relationship("Forecast", back_populates="city", lazy="joined")


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Integer)
    day = Column(Float)
    min = Column(Float)
    max = Column(Float)
    night = Column(Float)
    eve = Column(Float)
    morn = Column(Float)
    main = Column(String)
    description = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="forecasts", lazy="joined")

