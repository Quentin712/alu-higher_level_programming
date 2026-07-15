#!/usr/bin/python3
"""Defines a Square class that checks its size is valid."""


class Square:
    """A square that only accepts a valid size."""

    def __init__(self, size=0):
        """Create a new square, checking that size is a valid integer."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
