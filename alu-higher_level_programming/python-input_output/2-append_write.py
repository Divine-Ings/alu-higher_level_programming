#!/usr/bin/python3
"""Module 2-append_write.

Defines a function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    The file is created if it does not exist.

    Args:
        filename (str): the path of the file to append to.
        text (str): the string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
