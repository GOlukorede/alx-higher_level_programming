#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared = [element ** 2 for element in row]
        squared_matrix.append(squared)
    return squared_matrix
