#!/usr/bin/python3
"""Defines a class BaseGeometry with area and validation methods."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raise an exception since area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
