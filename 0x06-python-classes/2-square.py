#!/usr/bin/python3

"""
This module defines the Class Square
"""


class Square:
    """
    An empty class Square
    Attributes:
    none
    """
    def __init__(self, size=0):
        """
        This initializes the size of the square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        This initializes the area of the square
        """
        return self.__size * self.__size
