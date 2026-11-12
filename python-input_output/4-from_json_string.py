#!/usr/bin/python3
"""Module 4-from_json_string.

Defines a function that returns an object from a JSON string.
"""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): the JSON string to deserialize.
    """
    return json.loads(my_str)
