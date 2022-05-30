#!/usr/bin/python3
"""
    import base class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
    Rectangle class file
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

    def area(self):
        """
            calculates area
            Return: area
        """
        return self.__width * self.__height

    def __str__(self):
        """
            returns the rectangle description
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
