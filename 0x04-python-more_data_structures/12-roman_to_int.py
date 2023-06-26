#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    cur_var = 0
    res = 0
    prev = 0

    for char in list(roman_string):
        cur_var = dict.get(char)
        if cur_var < prev:
            res -= cur_var
        else:
            res += cur_var
        prev = cur_var
    
    return res


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

