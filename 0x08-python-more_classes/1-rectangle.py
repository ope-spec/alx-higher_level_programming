#!/usr/bin/python3
"""
A class that defines rectangle
"""


class Rectangle:
    """Aclass that represents rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with the given width and height
        Args:
        - width: The width of the rectangle. Default is 0.
        - height: The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set Rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
