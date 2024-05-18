#!/usr/bin/python3
"""A storage module."""
import json


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    # Class variables to hold file path and objects
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Return the dictionary __objects."""
        return __class__.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        __class__.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        dict_objs = {}
        for key in __class__.__objects:
            dict_objs[key] = __class__.__objects[key].to_dict()
        with open(__class__.__file_path, "w") as wr:
            json.dump(dict_objs, wr)

    def reload(self):
        """Deserialize the JSON file to __objects, only if the
        JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception is raised.
        """
        try:
            with open(__class__.__file_path) as rd:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                dict_objs = json.load(rd)
                # Deserialize objects based on class name
                for key in dict_objs:
                    if key.split(".")[0] == 'BaseModel':
                        __class__.__objects[key] = BaseModel(**dict_objs[key])
                    elif key.split(".")[0] == 'User':
                        __class__.__objects[key] = User(**dict_objs[key])
                    elif key.split(".")[0] == 'State':
                        __class__.__objects[key] = State(**dict_objs[key])
                    elif key.split(".")[0] == 'City':
                        __class__.__objects[key] = City(**dict_objs[key])
                    elif key.split(".")[0] == 'Amenity':
                        __class__.__objects[key] = Amenity(**dict_objs[key])
                    elif key.split(".")[0] == 'Place':
                        __class__.__objects[key] = Place(**dict_objs[key])
                    elif key.split(".")[0] == 'Review':
                        __class__.__objects[key] = Review(**dict_objs[key])
        except FileNotFoundError:
            pass
