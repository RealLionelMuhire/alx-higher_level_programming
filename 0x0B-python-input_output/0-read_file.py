#!/usr/bin/python3
"""reads the file and prints"""


def read_file(filename=""):
    """reads the file and prints output
        args:
            filename
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end="")
