#!/usr/bin/python3
"""Saves a Python object to a file, in JSON form."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a file."""
    with open(filename, "w", encoding="utf8") as f:
        json.dump(my_obj, f)
