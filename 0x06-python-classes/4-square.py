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
        self.__size = size

    @property
    def size(self):
        """
        a getter
        Return: self.__size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        a setter
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

    def area(self):
        """
        calculates area of a square
        Return: the result
        """
        result = self.__size * self.__size
        return result
