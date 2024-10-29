-- Cette commande crée un utilisateur nommé "user_0d_1" avec l'hôte "localhost" et un mot de passe "user_0d_1_pwd".
-- Le mot-clé "IF NOT EXISTS" permet de s'assurer que l'utilisateur n'est créé que s'il n'existe pas déjà.
CREATE USER IF NOT EXISTS 'user_0d_1@localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Cette commande accorde tous les privilèges sur toutes les bases de données et tables (*.*)
-- à l'utilisateur "user_0d_1" lorsqu'il se connecte depuis "localhost".
-- Cela lui permet d'exécuter toutes les actions (lecture, écriture, modification, suppression, etc.) sur la base de données.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1@localhost';