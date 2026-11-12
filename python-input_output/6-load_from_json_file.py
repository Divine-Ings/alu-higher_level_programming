#!/usr/bin/python3
"""Module 6-load_from_json_file.

Defines a function that creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): the path of the JSON file to read.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
