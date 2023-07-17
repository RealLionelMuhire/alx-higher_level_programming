#!/usr/bin/python3
"""returns the dictionary description with simple
data structure """


def class_to_json(obj):
    """returns the dictionary description with
        structure
        args: obj
        return: class dict
    """
    if (obj, "__dict__"):
        class_dict = obj.__dict__.copy()
        for key, value in class_dict.items():
            if not (isinstance(value, (list, dict, str, int, bool))):
                class_dict[key] = class_to_json(value)
            return class_dict
    else:
        return obj
