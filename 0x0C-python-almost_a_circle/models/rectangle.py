#!/usr/bin/python3
"""
    import base class
"""
from models.base import Base

"""
    Rectangle class file
"""


class Rectangle(Base):
    """
        create a class Rectangle which inherit of the baseclass Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initiate the Rectangle
            args:
                width
                height
                x: the position
                y: the position
                id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
            the getter function of the width
            return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            the setter function of the width
        """
        self.__width = value

    @property
    def height(self):
        """
            the getter function of the height
            return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            the setter function of the height
        """
        self.__height = value

    @property
    def x(self):
        """
            the getter function of x
            return x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            the setter function of x
        """
        self.__x = value

    @property
    def y(self):
        """
            the getter function of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            the setter function of y
        """
        self.__y = value
