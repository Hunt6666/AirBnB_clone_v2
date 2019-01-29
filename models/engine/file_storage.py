#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """deletes an object from the __objects if there"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if self.__objects[key] is not None:
                del self.__objects[key]

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object or all of a certain class
        """
        if cls is None:
            return self.__objects
        else:
            mydict = {}
            for k, v in self.__objects.copy().items():
                key = k
                if type(cls) == str:
                    if key.split('.')[0] == cls:
                        mydict[k] = v
                else:
                    if key.split('.')[0] == cls.__name__:
                        mydict[k] = v
            return mydict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """ calls reload for deserializing the Json file to objs """
        self.reload()
