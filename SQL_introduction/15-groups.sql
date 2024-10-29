-- Cette commande sélectionne les scores et compte le nombre d'occurrences de chaque score dans la table "second_table".
-- La fonction COUNT(score) est utilisée pour déterminer combien de fois chaque score apparaît.
-- Les résultats sont regroupés par score grâce à GROUP BY score,
-- puis triés par le nombre d'occurrences (number) en ordre décroissant.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;