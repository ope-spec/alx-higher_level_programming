#!/usr/bin/python3

"""class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
        Args:
            size: The size of the square. Defaults to 0.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
