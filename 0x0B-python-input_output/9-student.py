#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """Write a class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """instantiation idk """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public method that retieves a dictionary"""

        return self.__dict__
