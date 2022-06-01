#!/usr/bin/python3
"""
    a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
        creates an Object from a “JSON file”
        args:
            filename
    """
    with open(filename, "r", encoding="utf-8") as fo:
        return json.load(fo)