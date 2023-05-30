#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initializes a Square object with the given size.
        Args:
            size (int): The size of the square. Default is 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Args:
            value: The size of the square.
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

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square using the '#' character.
        If the size is 0, an empty line is printed.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
