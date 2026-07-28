#!/usr/bin/python3
"""Converts a Python object to its JSON string form."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
