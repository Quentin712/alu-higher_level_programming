#!/usr/bin/python3
"""Appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF8 file and return chars added."""
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
