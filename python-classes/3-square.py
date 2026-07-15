#!/usr/bin/python3
"""Defines a Square class that checks its size and can give its area."""


class Square:
    """A square that only accepts a valid size and knows its own area."""

    def __init__(self, size=0):
        """Create a new square, checking that size is a valid integer."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Give back the area of the square."""
        return self.__size * self.__size
