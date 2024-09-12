#!/usr/bin/python3
"""
Prints 'My name is' followed by the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is' followed by the first and last name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        say_my_name("John", "Doe") -> My name is John Doe
        say_my_name("Jane") -> My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Print the name, handling the case where the last name might be empty
    print("My name is {:s} {:s}".format(first_name, last_name))
