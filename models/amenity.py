#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
        Attributes:
                name = empty string
    """
    name = ""
    def __init__(self):
        """
            initializes a new Amenity class

            Attribute:
                *args, **kwargs
        """
        super.__init__(*args, **kwargs)
