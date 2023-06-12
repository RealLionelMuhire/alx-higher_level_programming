#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for subitem in item:
            if item.index(subitem) < len(item) - 1:
                print("{:d}".format(subitem), end=" ")
            else:
                print("{:d}".format(subitem), end="")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
