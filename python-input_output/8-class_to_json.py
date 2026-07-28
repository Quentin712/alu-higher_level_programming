#!/usr/bin/python3
"""Turns a class instance into a JSON-friendly dictionary."""


def class_to_json(obj):
    """Return a dict of an object's attributes for JSON use."""
    return obj.__dict__
