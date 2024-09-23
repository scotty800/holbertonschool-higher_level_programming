#!/usr/bin/python3
"""
Validates that the provided value is a positive integer.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Validates that the provided value is a positive integer.
    """
    def __init__(self, size):
        """
        Validates that the provided value is a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Validates that the provided value is a positive integer.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Validates that the provided value is a positive integer.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
