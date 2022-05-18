#!/usr/bin/python3
import math
class MagicClass:
    _MagicClass__radius = 0

    def __init__(self, radius):
        if radius is not type(int):
            raise TypeError("radius must be a number")
        if radius is not type(float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius
        return None
    def area(self):
        self._MagicClass__radius = (2 * self._MagicClass__radius) * math.pi
        return self._MagicClass__radius
    def circumference(self):
        self._MagicClass__radius =  self._MagicClass__radius * 2 * math.pi
        return self._MagicClass__radius
