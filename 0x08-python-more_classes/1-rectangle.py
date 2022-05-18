#!/usr/bin/python3
""" Function that defines a class Rectangle """


class Rectangle:
    """creates the class"""
    def __init__(self, width=0, height=0):
        """initializes the class"""
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value
