#!/usr/bin/python3
"""Module to divide all the elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix by a divisor
      Args:
          matrix (list): matrix to divide
      div (int): divisor
      Returns:
          list: matrix divided by divisor
    """

    if not matrix:
        raise ValueError("matrix must be a matrix (list of lists) of integers/floats")
    result_matrix = []
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise ValueError("Each row of the matrix must have the same size")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ValueError("division by zero")

        new_row = ["{:.2f}".format(j / div) for j in i]
        result_matrix.append(new_row)
    return result_matrix
