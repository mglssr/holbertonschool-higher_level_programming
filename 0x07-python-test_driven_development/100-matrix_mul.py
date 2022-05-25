#!/usr/bin/python3
"""Task 7"""


def matrix_mul(m_a, m_b):
    """function that mutiplies 2 matrices"""
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row1 in m_a:
        if not isinstance(row1, list):
            raise TypeError("m_a must be a list of lists")
        for a_n in row1:
            if not isinstance(a_n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row1) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row2 in m_b:
        if not isinstance(row2, list):
            raise TypeError("m_b must be a list of lists")
        for b_m in row2:
            if not isinstance(b_m, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
            if len(row2) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    try:
        result = 
    