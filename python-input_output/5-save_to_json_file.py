#!/usr/bin/python3
"""Module 5-save_to_json_file.

Defines a function that writes an object to a text file using JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a UTF-8 text file using its JSON representation.

    Args:
        my_obj: the object to serialize.
        filename (str): the path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
