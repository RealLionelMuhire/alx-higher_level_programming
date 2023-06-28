#!/usr/bin/python3
"""Create a class with size as attribute"""


class Square:
    """class of square"""
    def __init__(self, size=0):
        """initialization of Square and raise some errors
        args:
            size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """area of a circle
        args:
            None
        Return: the area of the circle"""
        return self.__size * self.__size
