#!/usr/bin/python3
""" Function that defines a class Rectangle """


class Rectangle:
    """creates the class"""
    def __init__(self, width=0, height=0):
        """initializes the class"""
        self.width = width
        self.height = height

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        out = ""
        if self.__width == 0 or self.__height == 0:
            return out
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    out += "#"
                out += "\n"
            return out[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
