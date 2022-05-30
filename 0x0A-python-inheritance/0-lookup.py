#!/usr/bin/python3
"""
    module of look up
"""


def lookup(obj):
    """
        returns the list of available attributes and methods of an object
    """
    li = dir(obj)
    return li
