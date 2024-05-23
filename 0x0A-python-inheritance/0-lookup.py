#!/usr/bin/python3
"""This module defines a function that returns the list"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
