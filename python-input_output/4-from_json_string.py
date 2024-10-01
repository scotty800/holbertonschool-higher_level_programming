#!/usr/bin/python3
"""
Converts a Python object to a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.
    Args:
    my_str (str): The JSON string to be converted.
    Returns:
    The corresponding Python object (e.g., dict, list, etc.)
    from the JSON string.
    """
    return json.loads(my_str)
