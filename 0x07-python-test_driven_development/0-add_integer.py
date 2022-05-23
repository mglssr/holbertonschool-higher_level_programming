#!/usr/bin/python3
"""test-driven development"""


def add_integer(a, b=98):
    """function that adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
