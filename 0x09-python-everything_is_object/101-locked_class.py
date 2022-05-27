#!/usr/bin/python3
"""
    LockedClass class file
"""


class LockedClass:
    """
        prevents the user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=0):
        """
            initiate the LockedClass
            args:
                fist_name: first_name of the LockedClass
        """
        self.first_name = first_name
