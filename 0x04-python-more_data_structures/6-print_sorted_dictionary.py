#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(a_dictionary)
    for key, value in sorted(new_dict.items()):
        print("{}: {}".format(key, value))
