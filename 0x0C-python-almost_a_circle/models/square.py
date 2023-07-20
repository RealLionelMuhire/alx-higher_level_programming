#!/usr/bin/python3
"""this contains the class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class square initializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns strings that display rectangle"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting size in square"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """updating the square"""
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
