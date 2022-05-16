#!/usr/bin/python3
"""
a function that divides 2 integers and prints the result
Arguments
    a: the numerator
    b: the denominator
Return: the value of the division, otherwise: None
"""


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
