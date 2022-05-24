#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest"""
    def tests(self):
        self.assertEqual(max_integer([1, 4, 10, 8]), 10)
    def test1(self):
        self.assertEqual(max_integer((1, 5, -50, 18)), 18)

if __name__ == '__main__':
    unittest.main()
