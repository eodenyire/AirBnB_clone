#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User  # Import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key in json_objects:
                    class_name = json_objects[key]["__class__"]
                    self.__objects[key] = eval(class_name)(**json_objects[key])
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        return {"BaseModel": BaseModel, "User": User}
