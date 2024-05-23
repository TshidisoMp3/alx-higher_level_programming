#!/usr/bin/python3
"""defines a  class check function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    if type(obj) == a_class:
        return True
    return False
