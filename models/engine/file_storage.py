#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place

class FileStorage:
    """defines a class fileStorage

        Attributes:
            __file_path: path of json file containing a class dict representation
            __objects: stores all obects in file_path
    """
    classes = {
        "BaseModel":BaseModel,
        "User":User,
        "Review": Review,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place
    }
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
                for key in deserialized_obj:
                    cls_name = deserialized_obj[key]["__class__"]
                    self.__objects[key] = eval(cls_name)(**deserialized_obj[key])
        except FileNotFoundError:
            pass
    def get_attr_name_from_classes(self, key):
        return self.classes.get(key)
