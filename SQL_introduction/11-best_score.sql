-- Cette requête sélectionne les colonnes "score" et "name" de la table "second_table"
-- et filtre pour afficher uniquement les enregistrements où "score" est supérieur ou égal à 10.
-- Les résultats sont triés par "score" dans l'ordre décroissant pour afficher les scores les plus élevés en premier.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;