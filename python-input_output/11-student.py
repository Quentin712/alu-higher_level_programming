#!/usr/bin/python3
"""Defines a Student class that can serialize and reload itself."""


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

    def reload_from_json(self, json):
        """Update this student's attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
