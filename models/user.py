#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
        defines a class User that inherits from BaseModel

        Attributes:
            email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            Initializes a new User class

            Args:
                *args, **kwargs
        """
        super().__init__(*args, **kwargs)
