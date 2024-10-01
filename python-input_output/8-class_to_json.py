#!/usr/bin/python3
"""
Renvoie le dictionnaire représentant une instance d'un objet.
"""


def class_to_json(obj):
    """
    Renvoie le dictionnaire représentant une instance d'un objet.
    Args:
    obj (object): Une instance d'une classe.
    Returns:
    dict: Un dictionnaire contenant les attributs de l'objet.
    """
    return obj.__dict__
