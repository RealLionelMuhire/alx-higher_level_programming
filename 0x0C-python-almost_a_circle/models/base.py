#!/usr/bin/python3
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
