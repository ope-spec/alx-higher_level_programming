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
            size (int, optional): The length of a side of the square (default is 0).
            position (tuple, optional): The position of the square as coordinates (default is (0, 0)).
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """
        Returns a string representation of the square using my_print().

        Returns:
            str: The string representation of the square.
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
        """
        Sets the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def pos_print(self):
        """
        Returns the position of the square as spaces.

        Returns:
            str: The position of the square.
        """
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
        """Prints the square in its position."""
        print(self.pos_print(), end='')
