#!/usr/bin/python3
"""
    add integer module
"""


def add_integer(a, b=98):
    """ Addition function
        Args:
        a: the first number
        b: the second number
        Return: the result
     """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile()
