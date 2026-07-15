#!/usr/bin/python3
"""Defines a Square class that can print itself at a given position."""


class Square:
    """A square with a checked size and a checked position on screen."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a new square with the given size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Give back the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set a new position, checking that it is a valid tuple."""
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Give back the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #, or a blank line if size is 0."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
