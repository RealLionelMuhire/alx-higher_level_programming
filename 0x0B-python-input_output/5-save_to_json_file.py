#!/usr/bin/python3
"""exporting json to file"""


def save_to_json_file(my_obj, filename):
    """save tp json file
    args:
        my_obj
        filename
        """
    import json
    with open(filename, 'w') as file:
        my_content = json.dumps(my_obj)
        file.write(my_content)
