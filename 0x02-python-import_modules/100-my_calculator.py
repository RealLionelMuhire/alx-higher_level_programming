#!/usr/bin/python3
from sys import argv, exit
import calculator_1 as calc
ln = len(argv)
if __name__ == "__main__":
    if ln < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    s = argv[2]
    if s == "+":
        print("{} {} {} = {}".format(a, s, b, calc.add(a, b)))
    elif s == "-":
        print("{} {} {} = {}".format(a, s, b, calc.sub(a, b)))
    elif s == "*":
        print("{} {} {} = {}".format(a, s, b, calc.mul(a, b)))
    elif s == "/":
        print("{} {} {} = {}".format(a, s, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
