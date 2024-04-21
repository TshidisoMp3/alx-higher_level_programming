#!/usr/bin/python3
"""
This module contains a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Returns the sum of two integers of a and b
    a and b must be integers or floats else typeError will be raised
    a and b must be casted to integers before addition of floats
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
