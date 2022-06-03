#!/usr/bin/python3
"""
    import class Rectangle
"""

from models.rectangle import Rectangle
"""
    square class file
"""


class Square(Rectangle):
    """
        creation of class Square that inherit of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initiates the square
            args:
                size: size of the square
                x: the ordinate
                y: the abcissa
                id: the id of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
            return the information of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
            return the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            the setter function of the size
        """
        self.width = value
        self.height = value
