#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The length of a side of the square.
        position (tuple): The position of the square as coordinates.

    Methods:
        area(): Calculates and returns the area of the square.
        pos_print(): Returns the position of the square as spaces.
        my_print(): Prints the square in its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        square_str = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            square_str += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                square_str += " "
            for j in range(self.size):
                square_str += "#"
            square_str += "\n"
        return square_str

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
