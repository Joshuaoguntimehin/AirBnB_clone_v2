#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
class State(BaseModel):
    """ State class """
    __tablename__ = 'state'
    name =Column(String(128), nullable=False)
    
    @property
    def cities(self):
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
                return city_list          