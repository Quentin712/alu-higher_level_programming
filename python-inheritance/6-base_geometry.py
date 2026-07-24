#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raise an exception since area is not implemented here."""
        raise Exception("area() is not implemented")
