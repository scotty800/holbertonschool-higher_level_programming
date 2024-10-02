#!/usr/bin/env python3
"""
Sérialise les données en JSON et les enregistre dans un fichier.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise les données en JSON et les enregistre dans un fichier.
    Args:
    data (any): Les données à sérialiser en format JSON.
    filename (str): Le nom du fichier dans lequel enregistrer les données.
    """
    with open(filename, 'w', encoding='utf-8') as fic:
        json.dump(data, fic)


def load_and_deserialize(filename):
    """
    Charge les données d'un fichier JSON et les désérialise.
    Args:
    filename (str): Le nom du fichier contenant les données JSON.
    Returns:
    any: Les données désérialisées depuis le fichier.
    """
    with open(filename, 'r', encoding='utf-8') as fic:
        return json.load(fic)
