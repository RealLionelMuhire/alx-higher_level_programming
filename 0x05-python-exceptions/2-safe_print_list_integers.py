#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for n in my_list:
            if i < x:
                if isinstance(n, int):
                    print("{:d}".format(n), end='')
                    i += 1
                else:
                    continue
            else:
                break
        print()
        return i
    except IndexError:
        print()
        return i
