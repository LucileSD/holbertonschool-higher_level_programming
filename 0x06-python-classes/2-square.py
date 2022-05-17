#!/usr/bin/python3
"""Square class file"""


class Square:
    """
        class Square defines a square
            Attributes:
                __size: the size of the square
    """
    __size = 0

    def __init__(self, size=0):
        """
        Init a square
        Args:
            size: the size of square
        Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
