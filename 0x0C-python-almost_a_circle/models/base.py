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
        """generic comment"""
        import json
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """generic comment"""
        if list_objs in None or len(list_objs) == 0:
            with open(cls.__name__ + '.json', "w") as _file:
                _file.write(cls.to_json_string(None))
        else:
            with open(cls.__name__ + '.json', "w") as _file:
                _file.write(cls.to_json_string([obj.to_dictionary()
                                                for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """generic comment"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
