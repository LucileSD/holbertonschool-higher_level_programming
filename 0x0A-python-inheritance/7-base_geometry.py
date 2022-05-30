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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
