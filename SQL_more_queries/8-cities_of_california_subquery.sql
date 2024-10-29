-- Cette commande sélectionne les colonnes "id" et "name" de la table "cities"
-- où l'identifiant de l'état (state_id) correspond à l'identifiant (id) de l'état
-- dont le nom est "California". 
-- Elle permet d'obtenir toutes les villes de Californie.
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');