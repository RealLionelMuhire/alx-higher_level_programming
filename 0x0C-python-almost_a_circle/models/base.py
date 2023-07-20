#!/usr/bin/python3
import json
"""the initial start of class base"""


class Base:
    """class is the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base init constructor
        args:
            id
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
 
    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs == [] or None:
                json.dump(list_objs, filename)
            else:
                j_string = cls.to_json_string([obj.to_dictionary() for obj
                                               in list_objs])
                file.write(j_string)
