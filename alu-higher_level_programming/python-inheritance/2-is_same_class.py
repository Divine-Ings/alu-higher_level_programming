#!/usr/bin/python3
"""Module 2-is_same_class.

Defines a function that checks if an object is exactly of a given class.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare with.

    Returns:
        True if type(obj) is a_class, otherwise False.
    """
    return type(obj) is a_class
