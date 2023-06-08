#!/usr/bin/python3
"""Function module that adds up 2 integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as an integer.
    Args:
    - a: first argument
    - b: second argument
    Raises:
    - TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
