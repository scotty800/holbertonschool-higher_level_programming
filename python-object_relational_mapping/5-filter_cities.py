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
    state_name = sys.argv[4]

    cursor = connection.cursor()
    """Création d'un objet curseur pour exécuter les commandes SQL"""

    cursor.execute(
        "SELECT cities.id, cities.name\
        FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC",
        (state_name,))

    """Récupération de toutes les lignes de résultat de la requête"""
    state = cursor.fetchall()
    
    print(", ".join(row[1] for row in state))

    cursor.close()
    connection.close()
