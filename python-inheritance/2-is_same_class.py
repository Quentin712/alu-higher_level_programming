#!/usr/bin/python3
"""Defines a function that checks the exact class of an object."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return type(obj) == a_class
