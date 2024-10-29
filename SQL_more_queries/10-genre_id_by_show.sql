-- Cette commande sélectionne le titre des émissions de télévision
-- à partir de la table "tv_shows" et l'identifiant de genre 
-- à partir de la table "tv_show_genres".
-- Elle utilise une jointure (JOIN) pour associer les émissions de télévision 
-- à leurs genres respectifs en reliant "tv_shows.id" à "tv_show_genres.tv_show_id".
-- Les résultats sont triés par le titre des émissions de télévision (tv_shows.title) 
-- en ordre croissant, puis par l'identifiant de genre (tv_show_genres.genre_id) en ordre croissant.
SELECT tv_shows.title, tv_shows_genres.genre.id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;