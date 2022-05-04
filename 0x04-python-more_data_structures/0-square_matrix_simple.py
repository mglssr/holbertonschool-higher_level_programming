#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = map(lambda x: x * x, matrix[i])
        new_matrix.insert(i, list(new_row))
    return new_matrix
