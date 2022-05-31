#!/usr/bin/python3
"""8. Rectangle"""


class BaseGeometry:
    """write a class BaseGeometry"""

    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """creates a inherited class from BaseGeometry"""

    def __init__(self, width, height):
        """initializing"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
