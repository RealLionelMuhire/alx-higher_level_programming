#!/usr/bin/python3
"""to JSON"""


def to_json_string(my_obj):
    """convert to json
    aergs:
        my_obj
    return: Jsondumps
    """
    import json
    return json.dumps(my_obj)
