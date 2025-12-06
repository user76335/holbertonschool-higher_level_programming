#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        if char in ".?:":
            print(char, end="\n\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        print(char, end="")
        i += 1
