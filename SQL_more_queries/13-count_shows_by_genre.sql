-- Cette commande sélectionne le titre des émissions de télévision
SELECT genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;