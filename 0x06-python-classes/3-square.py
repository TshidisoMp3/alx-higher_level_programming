#!/usr/bin/python3

"""
This module defines the Class Square
"""


class Square:
    """
    This class defines a square:
    - With a private instance attribute size
    - With a public instance method area
    - With a public instance method my_print
    - With a public instance method position
    - With a public instance method size
    - With a public instance method size
    """
class Square:
    """ Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
    