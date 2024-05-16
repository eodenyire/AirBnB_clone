#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """defines a class fileStorage

        Attributes:
            __file_path: path of json file containing a class dict representation
            __objects: stores all obects in file_path
    """
    def __init__(self):
        """class attributes initialized"""
        self.__file_path = 'file.json'#path to json file
        self.__objects = {}#empty dictionary

    def all(self):
        """returns the object __object"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj classname>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj #set key(<obj classname>.id) value(obj)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():#get obj from __objects
            obj_dict[key] = obj.to_dict()#serialize and store in obj_dict
        with open(self.__file_path, 'w')as file:
            json.dump(obj_dict, file)#write contents to file

    def reload(self):
        """"deserializes the JSON file to __objects if filepath exists"""
        try:
            with open(self.__file_path, 'r')as file:
                deserialized_obj = json.load(file)
                for key, value in deserialized_obj.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

