#!/usr/bin/python3
"""Create a class with size as attribute of instance"""


class Square:
    """Class of a square"""
    def __init__(self, size):
        """initialise the class, with its size
        args:
            size: size of the square"""
        self.__size = size
