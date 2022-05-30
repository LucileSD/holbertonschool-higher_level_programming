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
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            calculates area of a square
        """
        return self.__size ** 2
