#!/usr/bin/python3
"""Module 4-inherits_from.

Defines a function that checks if an object is an instance of a class that
inherited (directly or indirectly) from a given class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare with.

    Returns:
        True if the class of obj inherited from a_class, but is not
        a_class itself. Otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
