#!/usr/bin/python3
"""Module 0-read_file.

Defines a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): the path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
