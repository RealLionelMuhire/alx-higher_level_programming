#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for subitem in item:
            if item.index(subitem) < len(item) - 1:
                print("{:d}".format(subitem), end=" ")
            else:
                print("{:d}".format(subitem), end="")
        print()
