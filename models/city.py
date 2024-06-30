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

    