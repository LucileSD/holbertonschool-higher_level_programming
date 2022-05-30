#!/usr/bin/python3
"""
    import class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
    Square class file
"""


class Square(Rectangle):
    """
        defines a square
    """
    def __init__(self, size):
        """
            initiate a square
            args:
                size
        """
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size
        super().__init__(size, size)

    def area(self):
        """
            calculates area of a square
        """
        return self.__width ** 2

    def __str__(self):
        """
            prints the square description
        """
        return (f"[Square] {self.__width}/{self.__height}")
