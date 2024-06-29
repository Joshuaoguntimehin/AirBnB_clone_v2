#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(BaseModel):
    """ State class """
    __tablename__ = 'state'
    name =Column(String(128), nullable=False)