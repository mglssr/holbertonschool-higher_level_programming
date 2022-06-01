#!/usr/bin/python3
"""11. Student to disk and reload"""


class Student:
    """Write a class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """ssssssssssssssssh"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""

        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

        return self.__dict__

    def reload_from_json(self, json):
        """public method"""
        for key, value in json.items():
            self.__dict__[key] = value
