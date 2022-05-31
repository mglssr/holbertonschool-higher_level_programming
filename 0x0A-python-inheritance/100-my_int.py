#!/usr/bin/python3
"""12. My integer"""


class MyInt(int):
    """MyInt class that inherits from int class"""
    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
