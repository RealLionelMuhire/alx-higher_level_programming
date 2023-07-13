#!/usr/bin/python3
"""convert from json to str"""


def from_json_string(my_str):
    """convert from json to str
        args: my_str
        return: json dumps"""
    import json
    return json.loads(my_str)
