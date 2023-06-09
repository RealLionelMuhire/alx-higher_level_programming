#!/usr/bin/python3
def element_at(my_list, idx):
    ln = len(my_list)
    if idx < 0:
        return None
    elif idx >= ln:
        return None
    else:
        return my_list[idx]
