#!/usr/bin/python3
import json
"""Defines a JSON respresentation of an object."""

def to_json_string(my_obj):
    """Converts python object to json.

    Args:
        my_obj: object to be changed
    Return:
        json representation
    """
    return json.dumps(my_obj)
