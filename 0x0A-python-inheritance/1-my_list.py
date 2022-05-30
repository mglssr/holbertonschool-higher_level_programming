#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """Write a class MyList that inherits from list"""
    def print_sorted(self):
        """public instance method that print the bust but sorted"""
        print(sorted(self))
