#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return pi * self._radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        """
        return 2 * pi * self._radius


class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
