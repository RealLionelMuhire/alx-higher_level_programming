#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx in range(0, len(my_list) - 1):
        del my_list[idx]
        return my_list
    else:
        return my_list
