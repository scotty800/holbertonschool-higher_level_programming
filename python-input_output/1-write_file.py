#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.
    Args:
    filename (str): The name of the file to write to.
    Defaults to an empty string.
    text (str): The string to write to the file.
    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as fic:
        return fic.write(text)
