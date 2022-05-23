#!/usr/bin/python3
"""Matrix_divided"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    new_matrix=[]
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(j/div, 2) for j in row] for row in matrix]
