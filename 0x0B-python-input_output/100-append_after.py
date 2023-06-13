#!/usr/bin/python3
"""A function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_text=""):
    """
    Inserts text after each line containing a given string in a file.
    """
    updated_text = ""
    with open(filename) as file:
        for line in file:
            updated_text += line
            if search_string in line:
                updated_text += new_text
    with open(filename, "w") as file:
        file.write(updated_text)
