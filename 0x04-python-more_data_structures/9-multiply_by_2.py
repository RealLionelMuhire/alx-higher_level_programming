#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = {}
    for key, value in a_dictionary.items():
        n_dict[key] = list(map(lambda x: x * 2, value))
    return n_dict
