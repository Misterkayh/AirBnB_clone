#!/usr/bin/python3
"""
    FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

MY_CLS = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
}


class FileStorage:
    """ Serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Initializes instance """
        pass

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the
            JSON file (__file_path) exists ; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                self.__objects[key] = MY_CLS[value["__class__"]](**value)
                """ self.__objects[key] = BaseModel(**value) """
        except Exception:
            pass
