#!/usr/bin/python3

""" This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and : """

def text_indentation(text):

    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ".?:":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])
    print(text, end="")
