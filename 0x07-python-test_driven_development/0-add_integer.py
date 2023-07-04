#!/usr/bin/python3
"""adding 2 integers"""


def add_integer(a, b=98):
    """Return the sum of a and b, b is an optional arguments"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
