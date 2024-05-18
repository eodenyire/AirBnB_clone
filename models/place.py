#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """
        defines a class place

        Attributes:
            city_id, user_id, description, name, number_rooms, number_bathrooms, max_guest, price_by_night, 
            latitude, longitude, amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description =""
    numebr_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
