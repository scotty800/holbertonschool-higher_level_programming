#!/usr/bin/python3
"""
Loads an object from a text file containing JSON data.
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a text file containing JSON data.
    Args:
    filename (str): The name of the file to load from.
    """
    with open(filename, 'r', encoding="utf-8") as fic:
        return json.load(fic)
