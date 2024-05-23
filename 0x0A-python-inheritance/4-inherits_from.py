#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
