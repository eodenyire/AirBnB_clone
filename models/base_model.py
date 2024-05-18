#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    """Defines  all common attr and methods for all other classes"""

    def __init__(self, *args, **kwargs):  # updated
        """initializes an instance of base model based on JSON as **kwargs"""
        if kwargs:
            for key, value in kwargs.items():  # loop through kwargs dict
                if key != '__class__':
                    # get only created at and updated at keys
                    if key in ('created_at', 'updated_at'):
                        # convert string to obj
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # call to new method in file storage
            self._import_storage().new(self)

    def __str__(self):
        """print a string represantation of class"""
        class_name = self.__class__.__name__
        string_value = f"[{class_name}] ({self.id}) {self.__dict__}"
        print(string_value)
        return string_value

    def save(self):
        """updates updated_at with current time"""
        self.updated_at = datetime.now()
        self._import_storage().save()  # call to save method in file_storage

    def to_dict(self):
        """
            returns a dictionary,
            contains all key/values of __dict__ of the instance
        """
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation

    def _import_storage(self):
        """imports storage only when needed to prevent circular import error"""
        from models import storage
        return storage
