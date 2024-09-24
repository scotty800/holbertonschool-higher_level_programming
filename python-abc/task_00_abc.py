#!/usr/bin/env python3
"""
This module defines an abstract class Animal and
its concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to
        define the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog, inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a cat, inheriting from Animal.
    """
    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
