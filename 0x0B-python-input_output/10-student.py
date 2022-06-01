#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """Write a class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """aaaaaaaaaaaaaaaaaaaa"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""

        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

        return self.__dict__
