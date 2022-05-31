#!/usr/bin/python3
"""5. Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object to a text file,\
 using a JSON representation"""

    import json

    with open(filename, "w") as _file:
        return (_file.write(json.dumps(my_obj)))
