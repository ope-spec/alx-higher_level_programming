#!/usr/bin/python3
"""
Function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads the contents of a UTF8 text
    file and print to stdout
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
