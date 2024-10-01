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

    def to_json(self, attrs=None):
        """
        Renvoie un dictionnaire représentant l'étudiant.
        Returns:
        dict: Un dictionnaire contenant les attributs de l'instance.
        """
        if attrs is None:
            return self.__str__

        dict_n = {}
        for index in attrs:
            if index in attrs:
                dict_n[index] = self.__dict__[index]
        return dict_n
