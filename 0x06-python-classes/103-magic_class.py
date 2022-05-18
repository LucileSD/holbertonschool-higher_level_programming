#!/usr/bin/python3
"""Magicclass file"""
import math


class MagicClass:
    """
    MagicClass define a circle
    Attribute:
        _MagicClass__radius: radius of a circle
    """
    _MagicClass__radius = 0

    def __init__(self, radius):
        """
        Init a radius of a circle
        args:
            radius: the radius
            return: None
        """
        self._MagicClass__radius = 0
        if radius is not type(int) and radius is not type(float):
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius


    def area(self):
        """
        area calculates area of a circle
        return the calculation
        """
        return ((self._MagicClass__radius * 2) * math.pi)

    def circumference(self):
        """
        circumference calculates the circumference of a circle
        return the calculation
        """
        return (2 * math.pi * self._MagicClass__radius)
