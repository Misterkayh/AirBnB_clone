#!/usr/bin/python3
"""
    BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel:
            defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initializes instances of the BaseModel class """
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                                kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Returns human-readable representation of the object """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()

        return res
