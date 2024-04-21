#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from config import HBNB_TYPE_STORAGE
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
