#!/usr/bin/python3
"""This module has one function that opens a text file and prints what's inside it."""


def read_file(filename=""):
    """Open a UTF8 text file, read everything in it, and print it to the screen."""
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
