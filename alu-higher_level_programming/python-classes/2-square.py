#!/usr/bin/python3
"""Module 2-square.

Defines a class Square that represents a square with a validated size.
"""


class Square:
    """Represent a square defined by its private, validated size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
