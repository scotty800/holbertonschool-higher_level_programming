#!/usr/bin/python3
"""
Checks if an object is an instance of, or
if the object is an instance of
a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the
    object is an instance of
    a class that inherited from, the specified class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
    Returns:
        True if obj is an instance or inherited
        instance of a_class, False otherwise.
    """
    return type(obj) is a_class
