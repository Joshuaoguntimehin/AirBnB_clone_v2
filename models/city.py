#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(60), primary_key=True)
    state_id = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE`_STORAGE') == 'db':
        cities = relationship('city', backref-'state', cascade='all, delete-orphan')
    else:
        @property
        def citiec(self):
            import models
            from models.city import city
            city_list = []
            for city in models.storage.all(city).values():
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list