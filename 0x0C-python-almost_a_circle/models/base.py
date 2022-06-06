#!/usr/bin/python3
"""1. Base class"""


class Base:
    """Write the first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open('cls' + '.json', "w", encoding="utf-8") as _file:
            _file.write(Base.to_json_string(list_objs))
