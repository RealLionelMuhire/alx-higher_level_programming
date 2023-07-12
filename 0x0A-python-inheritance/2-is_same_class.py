#!/usr/bin/python3
"""true or false if they are from the same type"""


def is_same_class(obj, a_class):
    """is instance check for obj and class
    args:
        obj
        a_class
    Return: a bollean
    """
    return issubclass(obj, a_class)
