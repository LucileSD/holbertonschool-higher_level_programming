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

    @staticmethod
    def from_json_string(json_string):
        """
            the list of the JSON string
            args:
                json_string:  a string representing a list of dictionaries
            return:
                the list
        """
        list_repr = []

        if json_string is None:
            list_repr = []
        for inst in json.loads(json_string):
            list_repr.append(inst)
        return list_repr

    @classmethod
    def create(cls, **dictionary):
        """
            an instance with all attributes already set
            args:
                dictionary: can be thought of as a double pointer
                to a dictionary
            return:
                an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(2, 3)
        else:
            dummy_obj = cls(2)
        dummy_obj.update(**dictionary)
        return dummy_obj
