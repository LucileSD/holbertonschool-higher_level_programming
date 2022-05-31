#!/usr/bin/python3
import json
"""
    a function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
        args:
            myobj: the object
        return:
            the JSON representation
    """
    return json.dumps(my_obj)
