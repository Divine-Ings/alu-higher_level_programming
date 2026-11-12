#!/usr/bin/python3
"""Module 8-class_to_json.

Defines a function that returns the dictionary description of an object.
"""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are serializable.
    """
    return obj.__dict__
