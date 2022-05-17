#!/usr/bin/python3
"""Square class file"""


class Square:
    """
        class Square defines a square
            Attributes:
                __size: the size of the square
    """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """
        Init a square
        Args:
            size: the size of square
        Return: None
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        a getter
        Return: self.__position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        calculates area of a square
        Return: the result
        """
        result = self.__size * self.__size
        return result

    def my_print(self):
        """
        prints the square with '#'
        Return: None
        """
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            for k in range(self.__position[1]):
                print("")

        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
