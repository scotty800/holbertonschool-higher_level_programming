#!/usr/bin/python3
"""Connexion à la base de données MySQL
avec les informations
d'identification passées en arguments
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connexion à la base de données
    MySQL avec les informations
    d'identification passées en arguments
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = connection.cursor()
    """Création d'un objet curseur pour exécuter les commandes SQL"""

    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
            FROM cities\
                JOIN states ON cities.state_id = states.id")

    """Récupération de toutes les lignes de résultat de la requête"""
    state = cursor.fetchall()

    for row in state:
        print(row)

    cursor.close()
    connection.close()
