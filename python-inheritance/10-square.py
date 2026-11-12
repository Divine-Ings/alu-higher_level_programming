#!/usr/bin/python3
"""Module 10-square.

Defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square (positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
