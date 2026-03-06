#!/usr/bin/python3
"""Module for converting an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
