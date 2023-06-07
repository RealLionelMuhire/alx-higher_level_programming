#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        l_n = number % 10
        number = -number
    else:
        l_n = number % 10
    print("{}".format(l_n), end='')
    return l_n
