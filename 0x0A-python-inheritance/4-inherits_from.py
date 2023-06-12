#!/usr/bin/python3
"""
Check if an object is an instance of a class that
inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of a class that
    inherited (directly or indirectly); otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
