#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        # Check if n is a valid index
        return string
    else:
        # Create a new string without the character at index n
        return string[:n] + string[n+1:]
