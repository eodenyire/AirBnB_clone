#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
        defines a class Review

        Attributes:
            place_id, user_id, text

    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Initializes a class Review

            Attributes:
                *args, **kwargs
        """
        super().__init__(*args, **kwargs)
