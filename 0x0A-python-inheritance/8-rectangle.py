#!/usr/bin/python3
"""
    BaseGeometry class file
"""


class BaseGeometry:
    """
        creates a class base geometry
    """
    def area(self):
        """
            raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value
            args:
                name : is always a string
                value : an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        create a class Rectangle which inherit of the baseclass BaseGeometry
    """
    def __init__(self, width, height):
        """
            initiate the rectangle
            args:
                width
                height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
