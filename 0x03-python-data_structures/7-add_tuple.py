#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (1, 2)
    b = tuple_b + (1, 2)
    return (a[1] + b[1] + a[2] + b[2])
