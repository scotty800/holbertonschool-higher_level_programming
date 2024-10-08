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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with given width and height.
        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        :return: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either the width or height is 0, the perimeter is 0.
        :return: The perimeter of the rectangle (2 * (width + height)).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        print the print_symbol with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for index in range(self.__height):
            result += str(self.print_symbol) * self.width + "\n"
        return result.strip()

    def __repr__(self):
        """
        Returns a string representation that can be used to
        recreate the object.
        :return: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method that is called when an instance is deleted.
        It decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the larger area.
        If both are equal, returns rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
    Returns a new square-shaped Rectangle.

    Args:
        size (int): Size of the square's sides (default is 0).

    Returns:
        Rectangle: A new Rectangle instance with equal width and height.
    """
        return cls(size, size)
