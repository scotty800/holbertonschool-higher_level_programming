#!/usr/bin/python3
"""
Prints a square with the character '#' of a given size.
"""


def print_square(size):
    """
    Prints a square with the character '#' of a given size.

    Args:
        size (int): The size (length and width) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        print_square(3) will print:
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("#" * size)
