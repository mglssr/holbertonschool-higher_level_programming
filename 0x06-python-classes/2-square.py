#!/usr/bin/python3
""" function that defines a Square using a private instance attribute"""


class Square:
    """define the class"""
    def __init__(self, size=0):
        """ __init__ method runs as soon as an objet of a class is created.
        The method is useful to do any initialization (or passing initial
        values to your object) you want to do with your object."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
