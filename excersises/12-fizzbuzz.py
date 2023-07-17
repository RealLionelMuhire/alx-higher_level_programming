#!/usr/bin/python3
from docstring_generator import generate_docstring

def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=' ')
        elif n % 3 == 0:
            print("Fizz", end=' ')
        elif n % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(n), end=' ')


docstr = generate_docstring(fizzbuzz)
print(docstr)
