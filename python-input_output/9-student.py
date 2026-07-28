#!/usr/bin/python3
"""Defines a Student class that can describe itself as a dict."""


class Student:
    """Represents a student with a name and an age."""

    def __init__(self, first_name, last_name, age):
        """Set up a new student with their name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dict of this student's attributes for JSON use."""
        return self.__dict__
