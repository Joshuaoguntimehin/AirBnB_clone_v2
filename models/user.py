#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = column(string(128), nullable=false)
    password = column(string(128), nullable=false)
    first_name = column(string(128), nullable=false)
    last_name = column(string(128), nullable=false)
