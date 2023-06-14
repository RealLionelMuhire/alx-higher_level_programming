#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_mat = []
    n_mat = map(lambda row: list(map(lambda x: x ** 2, row)), matrix)
    return n_mat
