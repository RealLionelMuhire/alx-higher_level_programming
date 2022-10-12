#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer
value = "School"
printed = safe_print_integer(value)
if not printed:
    print(f"{value} is not an integer")
