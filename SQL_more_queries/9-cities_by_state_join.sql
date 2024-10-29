-- Cette commande sélectionne les colonnes "id" et "name" de la table "cities",
-- ainsi que le nom de l'état depuis la table "states".
-- Elle utilise une jointure (JOIN) pour associer les villes à leurs états respectifs
-- en reliant "cities.state_id" à "states.id".
-- Les résultats sont triés par l'identifiant des villes (cities.id) en ordre croissant.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;