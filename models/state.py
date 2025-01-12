#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ''

        @property
        def cities(self):
            """
            return the list of City objects from storage
            linked to the current State
            """
            from models import storage
            city_instances = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return city_instances
