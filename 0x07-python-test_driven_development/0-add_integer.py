#!/usr/bin/python3

"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """
    Return the sum of two integers or floats as integers.

    Args:
        a: first argument
        b: The second argument. Defaults to 98.

    Returns: The sum of the two arguments as an integer.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
