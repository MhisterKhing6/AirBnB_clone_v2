#! /usr/bin/env python3
import os.path
from os import path
import json
"""
Creates an engine to store BaseModel objects
"""


class FileStorage:
    """
    uses file to store BaseModel objects in json form
    class Variables:
        __objects : dictionary that store a Basemodel object by  using
                    <class name>.id as key
        __file_path:String path to json file
    public instance methods:
        all : returns __objects
        save : serialize __object to jason file
        new : Adds a BaseModel object to a __objects
        reload : deserialize json file to objects if __file_path exit
    """
    __objects = {}
    __file_path = 'file.json'

    def new(self, obj):
        """
        adds obj to __objects
        :param obj:
        :return: void
        """
        type(self).__objects["{}.{}".format(obj.__class__.__name__, obj.id)] =\
            obj

    def save(self):
        """
         serialize __objects to a file
        path
        :return:void
        """
        with open(type(self).__file_path, "w", encoding="utf-8") as file:
            save = {k: v.to_dict() for (k, v) in type(self).__objects.items()}
            json.dump(save, file)

    def allClass(self):
        """
        returns all classes and their references
        :return:
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        return {"BaseModel": BaseModel, "User": User,
                "State": State, "City": City,
                "Place": Place, "Review": Review,
                "Amenity": Amenity
                }

    def delete(self, obj=None):
        """delete object from __objects
        Args:
            obj: given object
        """
        if obj is None:
            return
        else:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def all(self, cls=None):
        """returns a dictionary
        Args:
            cls: class type to filter return by
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            nx = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    nx[key] = value
            return nx

    def reload(self):
        """serialize the file path to JSON file path
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """ deserializes the JSON file to objects
        """
        self.reload()

