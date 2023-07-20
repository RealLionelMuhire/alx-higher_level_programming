#!/usr/bin/python3
from models.base import Base
"""Rectangle class with its attributes"""


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class rectangle initializer"""
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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        i = 0
        for i in range(self.__height + self.__y):
            j = 0
            if i in range(self.__y):
                print()
            else:
                for j in range(self.__width + self.__x):
                    if j in range(self.__x):
                        print(" ", end='')
                    else:
                        print("#", end="")
                print()

    def __str__(self):
        """returns strings that display rectangle"""
        str = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/\
{self.height}"
        return str

    def update(self, *args, **kwargs):
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
        """rectangle dictionalry items"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.__height,
                'x': self.x,
                'y': self.y
                }


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
