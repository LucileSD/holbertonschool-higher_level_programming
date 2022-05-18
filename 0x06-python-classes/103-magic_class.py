#!/usr/bin/python3
"""Magicclass file"""
import math


class MagicClass:
    """
    MagicClass define a circle
    Attribute:
        _MagicClass__radius: radius of a circle
    """

    def __init__(self, radius=0):
        """
        Init a radius of a circle
        args:
            radius: the radius
            return: None
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """
        area calculates area of a circle
        return the calculation
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        circumference calculates the circumference of a circle
        return the calculation
        """
        return (2 * math.pi * self.__radius)
