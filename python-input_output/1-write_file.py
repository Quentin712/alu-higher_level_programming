#!/usr/bin/python3
"""Writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return chars written."""
    with open(filename, "w", encoding="utf8") as f:
        return f.write(text)
