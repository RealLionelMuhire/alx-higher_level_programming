#!/usr/bin/python3
"""class of Rectangle in python"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class represents a rectangle and
    inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The id of the Rectangle instance. If not provided, the
            Base.__nb_objects counter will be incremented
                      and used as the id.

        Raises:
            TypeError: If width, height, x, or y are not integers.
            ValueError: If width or height are not greater than 0,
            or if x or y are less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is None:
            super().__init__()
        else:
            self.id = id

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new value for the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new value for the height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The new value for the x-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The new value for the y-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters.

        The method prints the rectangle by iterating through the rows
        and columns
        and printing either spaces or '#' symbols based on the positions
        of __x, __y, __width, and __height.
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle in the format:
            "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/\
{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        The method can be called with positional arguments or
        keyword arguments.
        If called with keyword arguments, the corresponding attributes
        will be updated.
        If called with positional arguments, they will
        be used to update the attributes in the order:
        id, width, height, x, y.

        Args:
            *args: The positional arguments.
            **kwargs: The keyword arguments.

        Returns:
            None
        """
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        The dictionary contains the keys 'id', 'width', 'height', 'x', and 'y',
        with their corresponding attribute values.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.__height,
            'x': self.x,
            'y': self.y
        }
