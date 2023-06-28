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

    @property
    def size(self):
        """retrive the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size
        args:
            value
        Return: area of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        i = 0
        for i in range(self.__size):
            j = 0
            for j in range(self.__size):
                print("#", end='')
                j += 1
            print()
            i += 1
