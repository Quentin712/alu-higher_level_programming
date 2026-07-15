#!/usr/bin/python3
"""Defines a Square class with a size that is checked through a property."""


class Square:
    """A square whose size is controlled by a getter and setter."""

    def __init__(self, size=0):
        """Create a new square, checking that size is a valid integer."""
        self.size = size

    @property
    def size(self):
        """Give back the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size, checking that it is a valid integer."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Give back the area of the square."""
        return self.__size * self.__size
