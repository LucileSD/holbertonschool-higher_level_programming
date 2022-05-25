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
    if isinstance(a, int) or isinstance(a, float):
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        try:
            b = int(b)
        except Exception:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile()
