#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a given size and position.
        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square (default is (0, 0)).
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
            value (int): The size value to set.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: The position of the square in the format (x, y)."""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.
        Args:
            value (tuple): The position value to set.
        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
