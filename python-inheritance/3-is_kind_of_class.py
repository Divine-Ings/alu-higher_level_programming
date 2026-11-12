#!/usr/bin/python3
"""Module 3-is_kind_of_class.

Defines a function that checks if an object is an instance of a class
or of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare with.

    Returns:
        True if obj is an instance of a_class (or inherited), else False.
    """
    return isinstance(obj, a_class)
