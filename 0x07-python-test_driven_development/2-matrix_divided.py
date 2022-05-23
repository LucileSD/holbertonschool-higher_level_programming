#!/usr/bin/python3
"""
    Module to divide a matrix
"""


def matrix_divided(matrix, div):
    """devides all elements of a matrix"""
    new_matrix = []
    result = 0

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")

        result = []
        for num in range(len(lst)):
            if not isinstance(lst[num], int) and not\
              isinstance(lst[num], float):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
            result.append(round((lst[num] / div), 2))
        new_matrix.append(result)

    for mat1 in matrix:
        for mat2 in matrix:
            if len(mat1) != len(mat2):
                raise TypeError("Each row of the matrix must have the same"
                                " size")

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile()
