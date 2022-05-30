#!/usr/bin/python3
"""
    MyInt class file
"""


class MyInt(int):
    """
        MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __init__(self, value):
        """
            initiates MyInt
        """
        self.number = value

    def __eq__(self, other):
        """
            inverts == with !=
        """
        return self.number != other

    def __ne__(self, other):
        """
            inverts != with ==
        """
        return self.number == other
