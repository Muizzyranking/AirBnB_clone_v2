#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City

db = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'  # Always present, regardless of storage type
    name = Column(String(128), nullable=False)

    # For DBStorage
    if db == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    # For FileStorage
    else:
        @property
        def cities(self):
            """Returns """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
