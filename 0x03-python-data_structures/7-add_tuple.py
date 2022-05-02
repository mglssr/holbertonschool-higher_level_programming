#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    while len1 < 2:
       tuple_a = tuple_a + (0,)
       len1 += 1
    while len2 < 2:
        tuple_b = tuple_b + (0,)
        len2 += 1

    tuple_3 = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return(tuple_3)
