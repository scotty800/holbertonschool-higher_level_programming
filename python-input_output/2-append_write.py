#!/usr/bin/python3
"""
Appends a string to the end of a text file (UTF8) and
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and
    returns the number of characters added.
    Args:
    filename (str): The name of the file to append to.
    Defaults to an empty string.
    text (str): The string to append to the file.
    Returns:
    int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as fic:
        return fic.write(text)
