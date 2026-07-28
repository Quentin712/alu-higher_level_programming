#!/usr/bin/python3
"""Loads a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the Python object stored in a JSON file."""
    with open(filename, encoding="utf8") as f:
        return json.load(f)
