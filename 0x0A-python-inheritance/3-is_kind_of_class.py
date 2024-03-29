#!/usr/bin/python3
"""checks for insantance and sub"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or inherited from, the specified
        class; False otherwise.
    """
    return isinstance(obj, a_class)
