#!/usr/bin/python3
"""Module 6-base_geometry.

Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """Represent a base for geometry classes."""

    def area(self):
        """Compute the area (not implemented here).

        Raises:
            Exception: always, since area() is not implemented.
        """
        raise Exception("area() is not implemented")
