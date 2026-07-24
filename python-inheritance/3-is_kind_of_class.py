#!/usr/bin/python3
"""Defines a function that checks if an object is of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or one of its subclasses."""
    return isinstance(obj, a_class)
