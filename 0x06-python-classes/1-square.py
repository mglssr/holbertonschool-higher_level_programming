#!/usr/bin/python3
""" function that creates a class 'Square' that defines a square"""


class Square:
    """ define the class 'Square'"""
    def __init__(self, size):
        """ __init__ method runs as soon as an objet of a class is created.
        The method is useful to do any initialization (or passing initial
        values to your object) you want to do with your object."""
        self.__size = size
