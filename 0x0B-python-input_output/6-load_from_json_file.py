#!/usr/bin/python3
"""load from json"""


def load_from_json_file(filename):
    """load from json"""
    import json
    with open(filename, 'r') as file:
        j_data = file.read()
        my_obj = json.loads(j_data)
        return my_obj
