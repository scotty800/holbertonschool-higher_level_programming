#!/usr/bin/python3
"""
Writes an object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    using a JSON representation.
    Args:
    my_obj: The Python object to be written to the file.
    filename (str): The name of the file to write to.
    Returns:
    None
    """
    with open(filename, 'w', encoding="utf-8") as fic:
        json.dump(my_obj, fic)
