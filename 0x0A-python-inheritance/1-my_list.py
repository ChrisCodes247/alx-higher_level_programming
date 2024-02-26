#!/usr/bin/python3
"""Defines an inherited list class MYList."""


class MyList(list):
    """Implements sorted printing for the built in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        lst = self[:]
        print("{}".format(sorted(lst)))
