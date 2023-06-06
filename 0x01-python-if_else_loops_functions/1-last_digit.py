#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10

if number >= 0 and l_digit > 5:
    print("Last digit of", number, "is", l_digit, "and is greater than 5")
elif number >= 0 and l_digit == 0:
    print("Last digit of", number, "is", l_digit, "and is 0")
elif number >= 0 and l_digit < 6:
    print("Last digit of", number, "is", l_digit,
          "and is less than 6 and not 0")
elif number < 0:
    print("Last digit of", number, "is", -1 * l_digit,
          "and is less than 6 and not 0")
