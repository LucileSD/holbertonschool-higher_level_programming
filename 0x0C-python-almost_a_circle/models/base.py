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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            the JSON string representation of list_dictionaries
            args:
                list_dictionaries: list of dictionaries
            return: JSON string
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file
            args:
                list_objs: a list of instances who inherits of Base
        """
        list_dict = []
        str = ""

        if list_objs is None:
            list_objs = []
        for inst in list_objs:
            list_dict.append(inst.to_dictionary())

        str = cls.to_json_string(list_dict)

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as buf:
            buf.write(str)
