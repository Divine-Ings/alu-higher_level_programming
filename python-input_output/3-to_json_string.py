#!/usr/bin/python3
"""Module 3-to_json_string.

Defines a function that returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation (a string) of an object.

    Args:
        my_obj: the object to serialize.
    """
    return json.dumps(my_obj)
