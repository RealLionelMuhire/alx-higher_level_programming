#!/usr/bin/python3
"""class of rectangle"""


class Rectangle:
    """rectangle class is created"""

    def __init__(self, width, height):
        """initialization of rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """access the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """access the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
