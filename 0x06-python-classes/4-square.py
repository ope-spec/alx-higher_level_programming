#!/usr/bin/python3


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initializes a square object with a given size.
        Args:
            size (int): The size of the square's sides. Defaults to 0.
        """

        self.size = size

    @property
    def size(self):
        """Getter method for the size of the square's sides.
        Returns:
            int: The size of the square's sides.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size of the square's sides.
        Args:
            value (int): The size of the square's sides.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
