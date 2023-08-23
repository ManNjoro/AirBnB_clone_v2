#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models


class Amenity(BaseModel, Base):
    """ Class representing Amenity table"""
    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''
