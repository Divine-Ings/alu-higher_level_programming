#!/usr/bin/python3
"""Module 1-my_list.

Defines a class MyList that inherits from list.
"""


class MyList(list):
    """A list that can print itself sorted in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The list itself is not modified. All elements are assumed to be
        integers.
        """
        print(sorted(self))
