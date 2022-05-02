#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and not tuple_b:
        return tuple_a
    elif tuple_b and not tuple_a:
        return tuple_b
    elif not tuple_a and not tuple_b:
        tuple_3 = (0, 0)
        return tuple_3
    else:
        if len(tuple_a) < 2 and len(tuple_b) < 2:
            tuple_3 = (tuple_a[0] + tuple_b[0], 0)
            return tuple_3
        elif len(tuple_a) < 2 and len(tuple_b) >= 2:
            tuple_3 = (tuple_a[0] + tuple_b[0], tulpe_b[1])
            return tuple_3
        elif len(tuple_a) >= 2 and len(tuple_b) < 2:
            tuple_3 = (tuple_a[0] + tuple_b[0], tuple_a[1])
            return tuple_3
        else:
            tuple_3 = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
            return tuple_3
