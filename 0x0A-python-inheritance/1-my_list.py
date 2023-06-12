#!/usr/bin/python3
"""This module inherits from the list"""


class MyList(list):
    """A class MyList that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """funtion that prints a sorted list"""
        print(sorted(self))
