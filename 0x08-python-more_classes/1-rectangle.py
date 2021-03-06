#!/usr/bin/python3
"""Rectangle class file"""


class Rectangle:
    """
        creates a class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
            Init a rectangle
            args:
                width: the width of the rectangle
                height: the height of the rectangle
            Return: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            the getter of the width
            Return: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            the setter of the width
            args:
                value: the value for the width
            Return: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            the getter of height
            Return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            the setter of height
            args:
                value: the value for the height
            Return: None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
