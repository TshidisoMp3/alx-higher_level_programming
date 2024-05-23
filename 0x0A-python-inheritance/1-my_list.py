#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""

class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Print the list sorted."""
        print(sorted(self))
