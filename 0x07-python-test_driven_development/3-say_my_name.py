#!/usr/bin/python3
"""prints the name"""


def say_my_name(first_name, last_name=""):
    """
    prints the name as fist name and 2nd name
    Args:
        first_name: The first_name.
        last_name: the second name, empty when passed
    Raises:
        TypeError: if the first_name and the last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))