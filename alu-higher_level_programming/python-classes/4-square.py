#!/usr/bin/python3
"""Module 4-square.

Defines a class Square with a size accessible through a property.
"""


class Square:
    """Represent a square defined by its private, validated size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square.

        Raises:
            TypeError: if the value set is not an integer.
            ValueError: if the value set is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
