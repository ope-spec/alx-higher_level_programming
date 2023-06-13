#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
