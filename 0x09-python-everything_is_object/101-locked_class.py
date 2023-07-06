#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    prevents from creatin new attributes
    """

    __slots__ = ["first_name"]
