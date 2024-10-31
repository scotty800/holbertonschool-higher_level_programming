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
     host='localhost',
     port=330,
     user=sys.argv[1],
     password=sys.argv[2],
     database=sys.argv[3]
)

state_name_searched = sys.argv[4]

cursor = connection.cursor()

cursor.execute(
     "SELECT * FROM states WHERE NAME lIKE BINARY\
        '{}' ORDER BY id ASC".format(state_name_searched))

state = cursor.fetchall()

for row in state:
    print(row)

cursor.close()
connection.close()
