#!/usr/bin/python3
"""
    Base class file
"""
class Base:
    """
        base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            iniate the class Base
            args:
                id: an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
