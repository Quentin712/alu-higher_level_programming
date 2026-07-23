#!/usr/bin/python3
"""Defines a list class that can print itself sorted."""


class MyList(list):
    """A list of integers that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
