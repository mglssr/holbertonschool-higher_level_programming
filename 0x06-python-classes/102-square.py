#!/usr/bin/python3
"""Function that writes class Square"""


class Square:
    """Create the Square class"""
    def __init__(self, size=0):
        self.__size = size
        """Initializes the class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
		self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __lt__(self, comp):
        return self.area() < comp.area()

    def __le__(self, comp):
        return self.area() <= comp.area()

    def __eq__(self, comp):
        return self.area() == comp.area()

    def __ne__(self, comp):
        return self.area() != comp.area()

    def __ge__(self, comp):
        return self.area() >= comp.area()

    def __gt__(self, comp):
        return self.area() > comp.area()
