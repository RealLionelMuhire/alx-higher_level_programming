#!/usr/bin/python3
"""prints in sorted order"""


class MyList(list):
    """class that inherits a list"""

    def print_sorted(self):
        """prints a sorted list"""
        new_list = sorted(self)
        print(new_list)
