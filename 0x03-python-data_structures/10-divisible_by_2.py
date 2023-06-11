#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_lsit = []
    for element in my_list:
        if element % 2 == 0:
            n_lsit.append(True)
        elif element % 2 != 0:
            n_lsit.append(False)
    return n_lsit
