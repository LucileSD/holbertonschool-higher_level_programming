#!/usr/bin/python3
"""
    a function that returns an object (Python data structure)
    represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
        args:
            my_str : the string
        Return:
            an object represented by a JSON string
    """
    return json.loads(my_str)
