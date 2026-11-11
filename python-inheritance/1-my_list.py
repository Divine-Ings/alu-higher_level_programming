#!/usr/bin/python3

class MyList(list):
    """A custom list."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
