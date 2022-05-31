#!/usr/bin/python3
"""
    pascal trinagle function
"""


def pascal_triangle(n):
    """
        the Pascal’s triangle of n
        args:
            n: the number
        return:
            a list of lists of integers
    """
    triangle = []

    for lin in range(n):
        lis = []
        for idx in range(lin + 1):
            if idx == 0 or idx == lin:
                lis.append(1)
            else:
                lis.append(triangle[lin - 1][idx - 1] + triangle[lin - 1][idx])
        triangle.append(lis)

    return triangle
