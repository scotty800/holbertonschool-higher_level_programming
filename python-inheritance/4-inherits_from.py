#!/usr/bin/python3
"""
This module defines a function that checks if an object inherits from a class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class, but not an instance of the class itself.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance of a subclass of a_class,
        but not an instance of a_class.
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
