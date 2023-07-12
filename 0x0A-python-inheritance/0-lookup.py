#!/usr/bin/python3

def lookup(obj):
    """returns the list of available attributes in the obj
    args:
        obj: is the object module
    
    return:
        lsi of vabalable attr"""
    return dir(obj)
