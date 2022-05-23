#!/usr/bin/python3
"""Rectangle class file"""


class Rectangle:
    """
        creates a class that defines a rectangle
            Attributes:
                __width : the width of the rectangle
                __height: the height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Init a rectangle
            args:
                width: the width of the rectangle
                height: the height of the rectangle
            Return: None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            the getter of the width
            Return: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            the setter of the width
            args:
                value: the value for the width
            Return: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            the getter of height
            Return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            the setter of height
            args:
                value: the value for the height
            Return: None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            Calculate the area of the rectangle
            Return: the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            Calculate the perimeter of the rectangle
            Return: the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__height + self.__width) * 2
        return perimeter

    def __str__(self):
        """
            print the rectangle
            Return: the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join(str(self.print_symbol) * self.width
                         for i in range(self.height))

    def __repr__(self):
        """
            string representation
            Return: the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
            when attribute is deleted
            Return: None
        """
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
            defines the biggest rectangle
            Return: the biggest one
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
            defines a square
            return: a rectangle
        """
        return Rectangle(size, size)
