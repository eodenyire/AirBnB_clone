#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """
        defines a class state

        Attributes:
            name
    """
    name = ""

    def __init__(self):
        """
            initializes a class State

            Attribute:
                *args, **kwargs
        """
        super().__init__(*args, **kwargs)
