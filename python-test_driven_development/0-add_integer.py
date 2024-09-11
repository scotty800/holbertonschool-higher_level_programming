#!/usr/bin/python3
"""
this code we could to calculate an operation like add
"""


def add_integer(a, b=98):
    """
    Ajoute deux nombres, a et b, après les avoir convertis en entiers.
    Args:
        a: Le premier nombre, doit être un entier ou un flottant.
        b: Le second nombre, doit être un entier ou un flottant.
        Valeur par défaut = 98.
    Returns:
        La somme de a et b après conversion en entiers.
    Raises:
        TypeError: Si a ou b ne sont ni des entiers ni des flottants.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
