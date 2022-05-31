#!/usr/bin/python3
"""0. Read file"""


def read_file(filename="", mode="r", encoding="utf-8"):
    """function that reads text file and prints ir to stdout"""
    with open(filename) as _file:
        lines = _file.read()
        print(lines, end="")
