#!/usr/bin/python3
"""11. Square #2"""


class BaseGeometry:
    """write a class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """creates a inherited class from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """creates a inherited class from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return(f"[Square] {self.__size}/{self.__size}")
