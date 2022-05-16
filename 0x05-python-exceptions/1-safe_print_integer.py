#!/usr/bin/python3
"""
 a function that prints an integer
 Arguments:
    value: the number to print
Return: True if it is an integer, False otherwise
"""


def safe_print_integer(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
        except Exception:
            return False
        return True
