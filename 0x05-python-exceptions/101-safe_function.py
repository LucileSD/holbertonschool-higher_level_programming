#!/usr/bin/python3
import sys
"""
a function that executes a function safely
Arguments:
    fct: a pointer to a function
    args: argument
Return: the result of the function, Otherwise, returns None
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
