#!/usr/bin/python3
"""
     a function that returns the dictionary description with simple
     data structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object
"""


def class_to_json(obj):
    """
         a function
         args:
            obj : the object, an instance of a Class
        return:
            the dictionary description with simple data structure
    """
    return obj.__dict__
