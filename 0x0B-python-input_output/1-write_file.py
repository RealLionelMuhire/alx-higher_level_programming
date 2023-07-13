#!/usr/bin/python3
"""write"""


def write_file(filename="", text=""):
    """wirte and return number of char written"""

    with open(filename, 'w') as file:
        return file.write(text)
