#!/usr/bin/python3
"""class of rectangle"""


class Rectangle:
    """rectangle class is created"""

    def __init__(self, width=0, height=0):
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

    def area(self):
        """computing the area"""

        return self.__height * self.__width

    def perimeter(self):
        """computing the perimeter"""

        if self.__width == 0 and self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a string representation of a rectangle"""
        recta = ""
        unit = 0
        while unit < self.height:
            wid = 0
            while wid < self.width:
                recta += "#"
                wid += 1
            recta += "\n"
            unit += 1
        return recta

    def __repr__(self):
        """Return the official string representation of a rectangle
        This can be used to recreate it"""

        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """Detect object deletion"""
        print("Bye rectangle...")