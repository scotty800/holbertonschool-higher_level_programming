#!/usr/bin/python3
"""
    Class representing a square with size validation,
    a getter/setter for the size, and an area calculation method.
"""


class Square:
    """
    Class representing a square with size validation,
    a getter/setter for the size, and an area calculation method.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square with a given size.
        :param size: The length of the side of the square (default is 0).
        """
        self.__size = size
        self.__postion = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        :return: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square and validates it.
        :param value: The new size of the square.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        :return: The area of the square (size^2).
        """
        return self.__size ** 2

    @property
    def postion(self):
        return self.__postion

    @postion.setter
    def position(self, value):
        """
        Sets the position of the square and validates it.
        :param value: The new position of the square.
        :raises TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using '#' characters.
        If the size of the square is 0, prints an empty line.
        The position attribute determines the spacing of the square.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
