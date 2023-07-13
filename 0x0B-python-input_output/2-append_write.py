#!/usr/bin/python3
"""Appending"""


def append_write(filename="", text=""):
    """write and append, without deleting
    args:
    filename : filename
    text: text to write
    """
    with open(filename, 'a') as file:
        return file.write(text)
