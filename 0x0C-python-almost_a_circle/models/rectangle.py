#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The identity of the rectangle. Defaults to None.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y is not positive.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Gets or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    @property
    def y(self):
        """Gets or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle using the '#' character.

        Example:
            # # # #
            # # # #
            # # # #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the rectangle's attributes.

        Args:
            *args (int): New attribute values in the following order:
                - 1st argument represents the id attribute
                - 2nd argument represents the width attribute
                - 3rd argument represents the height attribute
                - 4th argument represents the x attribute
                - 5th argument represents the y attribute
            **kwargs (int): New attribute values passed as key-value pairs.

        Example:
            rectangle.update(1, width=10, height=5)
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
