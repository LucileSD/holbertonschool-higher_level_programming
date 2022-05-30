#!/usr/bin/python3
"""
    creattion of a function to add attributes
"""


def add_attribute(obj, attribute, value):
    """
        adds a new attribute to an object if it’s possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
