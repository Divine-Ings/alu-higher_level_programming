#!/usr/bin/python3
"""Module 1-square.

Defines a class Square that represents a square with a private size.
"""


class Square:
    """Represent a square defined by its private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the new square (no validation).
        """
        self.__size = size
