#!/usr/bin/python3
"""divide all elements of matrix"""


def matrix_divided(matrix, div):
    """
    Matrix divider function, devide all elements by div
    
    Args:
        matrix: list of lists
        div: divisor
    Return: a devided matrix
    
    Raises:
        TypeErrors: if its not appropriate type
        ZeroDivisionError: when div is 0
        """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size") 
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero") 
    new_mat = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_mat.append(new_row)
    return new_mat


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
