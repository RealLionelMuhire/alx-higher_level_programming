#!/usr/bin/python3
def roman_to_int(roman_string):
    letters = ["I", "V", "X", "L", "C", "D", "M"]
    rom_num = reversed(letters)
    digits = [1, 5, 10, 50, 100, 500, 1000]
    numbers = reversed(digits)
    int(n)
    idx = 0
    if roman_string not in rom_num or roman_string == "":
        return 0
    for char in list(roman_string):
        for var in rom_num:
            if char == var:
                if rom_num.index(var)
                n = numbers[rom_num.index(var)]
    
