#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def load_from_json_file(filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        data = f.read()
        return json.loads(data)
