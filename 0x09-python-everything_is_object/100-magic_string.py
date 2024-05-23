#!/usr/bin/python3
"""Function that returns a string "Holberton" n times"""


def magic_string(n=[0]):
    n[0] += 1
    return "Holberton, " * (n[0] - 1) + "Holberton"
