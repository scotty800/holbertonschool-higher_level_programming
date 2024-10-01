#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.
    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as fic:
        print(fic.read(), end="")
