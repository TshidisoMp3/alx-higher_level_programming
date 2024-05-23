#!/usr/bin/python3
"""This module defines a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
