#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Check if obj's class is a subclass of a_class, but not a_class itself."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
