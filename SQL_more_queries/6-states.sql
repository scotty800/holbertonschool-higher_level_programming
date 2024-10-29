-- Crée une base de données nommée "hbtn_0d_usa" si elle n'existe pas déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utilise la base de données "hbtn_0d_usa" pour exécuter les commandes suivantes.
USE hbtn_0d_usa;
-- Crée une table nommée "states" si elle n'existe pas déjà, avec les colonnes suivantes :
-- "id" est un entier (INT) avec une auto-incrémentation (AUTO_INCREMENT), 
-- ce qui permet de générer automatiquement une valeur unique pour chaque nouvel enregistrement. 
-- Il est aussi défini comme clé primaire (PRIMARY KEY) et ne peut pas être NULL (NOT NULL).
-- "name" est un champ texte (VARCHAR) pouvant contenir jusqu'à 256 caractères et ne peut pas être NULL.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);