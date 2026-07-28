#!/usr/bin/python3
"""Opens a text file and prints its contents."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents."""
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")
