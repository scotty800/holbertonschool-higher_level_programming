-- Cette commande crée une table nommée "unique_id" avec deux colonnes :
-- "id" de type entier (INT) avec une contrainte UNIQUE et une valeur par défaut de 1.
-- La contrainte UNIQUE garantit que chaque valeur de "id" est unique dans la table, empêchant ainsi les doublons.
-- "name" est une colonne de type chaîne de caractères (VARCHAR) pouvant contenir jusqu'à 256 caractères.
CREATE TABLE unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));