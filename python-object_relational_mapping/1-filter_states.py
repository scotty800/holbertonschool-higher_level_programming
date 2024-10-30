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
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()
    """Création d'un objet curseur pour exécuter les commandes SQL"""

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    """Récupération de toutes les lignes de résultat de la requête"""
    state = cursor.fetchall()

    for row in state:
        print(row)

    cursor.close()
    db.close()
