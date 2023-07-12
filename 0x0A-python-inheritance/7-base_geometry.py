#!/usr/bin/python3
"""Base geometry"""


class BaseGeometry:
    """class of Geomtry"""

    def area(self):
        """rectangle area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate int
        args:
            name: name
            value: value
        Return: validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
