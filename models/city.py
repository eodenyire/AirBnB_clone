#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
        defines a class city
        Attributes:
            state_id, name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
            initializes a class City

            Attributes:
                *args, **kwargs
        """
        super().__init__(*args, **kwargs)
