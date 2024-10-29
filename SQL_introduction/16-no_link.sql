-- Cette commande sélectionne les colonnes "score" et "name" de la table "second_table"
-- en filtrant les enregistrements pour n'inclure que ceux où la colonne "name" n'est pas nulle.
-- Les résultats sont ensuite triés par "score" dans l'ordre décroissant,
-- ce qui permet d'afficher les scores les plus élevés en premier.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;