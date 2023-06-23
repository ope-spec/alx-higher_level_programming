#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The identity of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets or sets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes.

        Args:
            *args (int): New attribute values in the following order:
                - 1st argument represents the id attribute
                - 2nd argument represents the size attribute
                - 3rd argument represents the x attribute
                - 4th argument represents the y attribute
            **kwargs (int): New attribute values passed as key-value pairs.

        Example:
            square.update(1, size=10, x=2)
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
