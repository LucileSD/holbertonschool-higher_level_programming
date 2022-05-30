#!/usr/bin/python3
"""
    MyList class file
"""


class MyList(list):
    """
        a class MyList that inherits from list
    """

    def print_sorted(self):
        """
            prints a sorted list
        """
        print(sorted(self))
