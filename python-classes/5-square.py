#!/usr/bin/python3
"""Defines a Square class that can print itself using # characters."""


class Square:
    """A square that can check its size and print itself out."""

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

    def my_print(self):
        """Print the square with #, or a blank line if size is 0."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
