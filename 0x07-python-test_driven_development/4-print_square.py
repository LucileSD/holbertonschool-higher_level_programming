#!/usr/bin/python3
"""
    Module to print a square
"""


def print_square(size):
    """prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print(f"#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile()
