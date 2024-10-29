-- Cette commande crée une table nommée "id_not_null" avec deux colonnes :
-- "id" de type entier (INT) avec une largeur de 1 chiffre, servant de clé ou identifiant pour chaque enregistrement.
-- "name" est de type chaîne de caractères (VARCHAR) pouvant contenir jusqu'à 256 caractères.
-- Par défaut, aucune contrainte "NOT NULL" n'est définie sur "id", il est donc possible que la colonne "id" contienne des valeurs NULL.
CREATE TABLE id_not_null (id INT(1), name VARCHAR(256));