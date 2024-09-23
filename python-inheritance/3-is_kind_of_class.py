#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class or a class that it inherits from.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or
    a class that a_class inherits from.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance or
        inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
