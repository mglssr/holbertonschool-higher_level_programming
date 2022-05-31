#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text file\
and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as _file:
        return (_file.write(text))
