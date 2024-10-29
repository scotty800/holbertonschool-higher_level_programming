-- Cette commande crée une base de données nommée "hbtn_0d_2" si elle n'existe pas déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Cette commande crée un utilisateur nommé "user_0d_2" avec l'hôte "localhost" et un mot de passe "user_0d_2_pwd".
-- Le mot-clé "IF NOT EXISTS" permet de s'assurer que l'utilisateur n'est créé que s'il n'existe pas déjà.
CREATE USER IF NOT EXISTS  'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Cette commande accorde uniquement le privilège SELECT (lecture) sur toutes les bases de données et tables (*.*)
-- à l'utilisateur "user_0d_2" lorsqu'il se connecte depuis "localhost".
GRANT SELECT ON hbtn_0d_2.* TO `user_0d_2`@`localhost`;