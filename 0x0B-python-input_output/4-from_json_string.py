#!/usr/bin/python3
"""Defines a JSON-to-string function."""
import json


def to_json_string(my_obj):
    """Return the python object represented by a JSON string."""
    return json.loads(my_obj)
