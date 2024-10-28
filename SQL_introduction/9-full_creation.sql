-- Création de la table "second_table" avec trois colonnes :
-- "id" de type entier (INT), "name" de type chaîne de caractères (VARCHAR) pouvant contenir jusqu'à 256 caractères,
-- et "score" de type entier (INT) pour stocker des scores.
CREATE TABLE second_table(id INT, name VARCHAR(256), score INT);
-- Insertion de plusieurs lignes dans la table "second_table" avec des valeurs spécifiques pour chaque colonne :
-- "id" identifiant chaque ligne, "name" pour le nom de la personne, et "score" pour le score associé.
INSERT INTO second_table(id, name, score)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);