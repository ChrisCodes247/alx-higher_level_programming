#!/usr/bin/python3

"""
A function that divides a matrix.
"""

def matrix_divided(matrix, div):
    """Divide a matrix by div.

    Args:
        matrix - a matrix of type integer.
        div (int) - integer that divides the matrix.

    Return: the modified matrix
    """
    modified_matrix = []
    reference_row = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != reference_row:
          raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, str):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        modified_row = []
        #print(row)
        for element in row:
            #print(element)
            if isinstance(element, str):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res = round(element / div, 2)
            modified_row.append(res)
        modified_matrix.append(modified_row)
    return (modified_matrix)
