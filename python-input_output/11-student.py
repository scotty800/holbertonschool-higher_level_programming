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
        dict: Un dictionnaire ontenant les attributs de l'instance.
        """
        if attrs is None:
            return self.__dict__

        dict_n = {}
        for index in attrs:
            if index in self.__dict__:
                dict_n[index] = self.__dict__[index]
        return dict_n

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'instance
        par ceux du dictionnaire 'json'.
        Args:
        json (dict): Un dictionnaire
        contenant des paires clé-valeur
        représentant les nouveaux attributs
        et valeurs à mettre à jour
        pour l'instance.
        """
        for key, value in json.items():
            self.__dict__[key] = value
