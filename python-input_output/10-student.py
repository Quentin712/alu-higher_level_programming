#!/usr/bin/python3
"""Defines a Student class that can describe itself as a dict."""


class Student:
    """Represents a student with a name and an age."""

    def __init__(self, first_name, last_name, age):
        """Set up a new student with their name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict of this student's attributes for JSON use."""
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
