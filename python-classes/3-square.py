#!/usr/bin/python3
"""
Class representing a square with size validation.
"""


class Square:
    """
    Class representing a square with size validation.
    """
    def __init__(self, size=0):
        """
        Initializes the Square with a given size, and validates it.

        :param size: The length of the side of the square (default is 0).
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates and returns the area of the square.
        :return: The area of the square (size * size).
        """
        return self.__size * self.__size
