-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
	JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE name NOT IN
	(
		SELECT name
		FROM tv_genres
		JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
		JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
		WHERE title = 'Dexter'
	)
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
