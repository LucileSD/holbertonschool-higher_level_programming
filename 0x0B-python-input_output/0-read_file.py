#!/usr/bin/python3
"""
    read a text file
"""


def read_file(filename=""):
    """
        a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as fo:
        for line in fo:
            print(line, end="")
