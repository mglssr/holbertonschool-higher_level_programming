#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file\
    and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as _file:
        return (_file.write(text))
