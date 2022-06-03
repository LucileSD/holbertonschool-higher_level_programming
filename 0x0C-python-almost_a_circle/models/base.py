#!/usr/bin/python3
"""
    import module json
"""
import json

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

    def to_json_string(list_dictionaries):
        """
            the JSON string representation of list_dictionaries
            args:
                list_dictionaries: list of dictionaries
            return: JSON string
        """
        return json.dumps(list_dictionaries)
