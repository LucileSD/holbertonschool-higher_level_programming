#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
    Recatangle class file
"""


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
