#!/usr/bin/python3
"""checks for inheritance"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
    args:
        obj
        a_class
    Return: a boolean
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
