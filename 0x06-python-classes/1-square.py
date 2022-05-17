#!/usr/bin/python3
"""Square class file"""


class Square:
    """
        class Square defines a square
        Attributes:
            __size: the size of the square
    """
    __size = 0

    def __init__(self, size):
        """
        Init a square

        Args:
            size (int): size of the square

        Returns: None
        """
        self.__size = size
