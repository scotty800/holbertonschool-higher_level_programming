#!/usr/bin/python3
"""
Classe représentant un étudiant.
"""


class Student:
    """
    Classe représentant un étudiant.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation des attributs de l'étudiant.
        Args:
        first_name (str): Prénom de l'étudiant.
        ast_name (str): Nom de famlle de l'étudiant.
        age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Renvoie un dictionnaire représentant l'étudiant.
        Returns:
        dict: Un dictionnaire contenant les attributs de l'instance.
        """
        return self.__dict__
