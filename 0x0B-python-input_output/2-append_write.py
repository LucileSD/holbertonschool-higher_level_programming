#!/usr/bin/python3
"""
    appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file
        args:
            filename : the file to open
            text: the text to write
        Return:
            the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as fo:
        return fo.write(text)
