#!/usr/bin/python3
"""
Class representing a rectangle.
"""


class Rectangle:
    """
    Class representing a rectangle.
    This class provides getter and setter methods for the width and height,
    with validation to ensure positive integers.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with given width and height.
        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        :return: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle and validates it.
        :param value: The new width of the rectangle.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        :return: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle and validates it.
        :param value: The new height of the rectangle.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
