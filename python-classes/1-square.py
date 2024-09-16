#!/usr/bin/python3
"""
Class representing a square with a private size attribute.
"""


class Square:
    """
    Class representing a square with a private size attribute.
    """
    def __init__(self, size):
        """
        Initializes the Square with a given size.
        :param size: The length of the side of the square.
        """
        self.__size = size
