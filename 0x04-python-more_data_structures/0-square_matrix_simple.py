#!/usr/bin/python3

new_matrix = []
def square_matrix_simple(matrix=[]):
    ''' computes the square value of all integers of a matrix'''
    for num in matrix:
        squared_row = [element ** 2 for element in num]
        new_matrix.append(squared_row)
    return (new_matrix)
