#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
import models


class Place(BaseModel, Base):
    """ A place to stay """
    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False,)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.HBNB_TYPE_STORAGE != 'db':
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id"""
            from models.review import Review
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id
            linked to the Place"""
            return [
                amenity for amenity in models.storage.all(Amenity).values()
                if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute that handles append method for adding
            an Amenity.id to the attribute amenity_ids"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
