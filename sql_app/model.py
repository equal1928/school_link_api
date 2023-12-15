from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Flat(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True, index=True)
    floor = Column(Integer, index=True)
    price = Column(Integer)
    square = Column(Integer)
    house_id = Column(Integer, ForeignKey("houses.id"))
    url = Column(String, unique=True, index=True)

    house = relationship("House", back_populates="flats")


class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    year_of_building = Column(Integer, index=True)
    #wall_material = Column(String, index=True)
    is_new = Column(Boolean)
    school = relationship("School", back_populates="owner")
    longitude = Column(Float)
    latitude = Column(Float)


class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    initial_data = Column(Integer, index=True)
    amount_of_students = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)
