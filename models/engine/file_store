#!/usr/bin/python3
"""A storage module.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        dict_objs = {}
        for key in FileStorage.__objects:
            dict_objs[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as wr:
            json.dump(dict_objs, wr)

    def reload(self):
        """Deserializes the JSON file to __objects. only if the
        JSON file (__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception raised
        """
        try:
            with open(FileStorage.__file_path, "r") as rd:
                dict_objs = json.load(rd)
                for key, value in dict_objs.items():
                    cls_name = value["__class__"]
                    cls = self.classes.get(cls_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

