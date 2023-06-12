#!/usr/bin/python3

"""a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square that inherits from rectangle"""

    def __init__(self, size):
        """Initialize a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
