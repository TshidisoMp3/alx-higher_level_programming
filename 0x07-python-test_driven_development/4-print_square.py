#!/usr/bin/python3
""" This module contains a function that prints a square with the character # """

def print_square(size):

    """
    Prints a square with the character #
    size must be an integer
    size must be greater than or equal to 0
    size must be a number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
