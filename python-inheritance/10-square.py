#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square defined by a positive integer size."""

    def __init__(self, size):
        """Initialize a new square with a validated size."""
        super().__init__(size, size)
