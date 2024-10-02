#!/usr/bin/env python3
"""
Initialise un objet CustomObject
avec un nom, un âge, et un statut étudiant.
"""


import pickle
"""
Initialise un objet CustomObject
avec un nom, un âge, et un statut étudiant.
"""


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialise un objet CustomObject avec
        un nom, un âge, et un statut étudiant.
        Args:
        name (str): Le nom de la personne.
        age (int): L'âge de la personne.
        is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet CustomObject."""
        print("Name: {}\nAge: {}\nIs Student: {}\n"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Sérialise l'objet courant et le sauvegarde dans un fichier.
        Args:
        filename (str): Le nom du fichier dans
        lequel l'objet doit être sauvegardé.
        """
        with open(filename, 'wb') as fic:
            pickle.dump(self, fic)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet CustomObject depuis un fichier.
        Args:
        filename (str): Le nom du fichier contenant l'objet sérialisé.
        Returns:
        CustomObject: L'objet désérialisé depuis le fichier.
        """
        try:
            with open(filename, 'rb') as fic:
                return pickle.load(fic)
        except Exception:
            return None
