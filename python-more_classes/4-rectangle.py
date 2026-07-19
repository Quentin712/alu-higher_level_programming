#!/usr/bin/python3
"""This file has a class for a rectangle with a width and a height."""


class Rectangle:
    """A rectangle that checks its width and height are valid."""

    def __init__(self, width=0, height=0):
        """Set up a new rectangle with the given width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Give back the current width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking it is a valid whole number."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Give back the current height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking it is a valid whole number."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Work out and give back the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Work out and give back the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Draw the rectangle using the # character, row by row."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = [("#" * self.__width) for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Give back text that can rebuild this same rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
