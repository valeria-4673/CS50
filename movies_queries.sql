1. SELECT title FROM movies WHERE year = 2008;
2. SELECT birth FROM people WHERE name = 'Emma Stone';
3. SELECT title FROM movies WHERE year >= 2018 ORDER BY title;
4. SELECT COUNT(*) FROM ratings WHERE rating = 10;
5. SELECT title, year FROM movies WHERE title LIKE '%Harry Potter%' ORDER BY year;
6. SELECT AVG(rating) FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2012;
7. SELECT rating, title
FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2010
ORDER BY rating DESC, title;
8. SELECT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE title = 'Toy Story';
9. SELECT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE year = 2004
ORDER BY birth;
10. SELECT name FROM people
JOIN directors ON people.id = directors.person_id
JOIN ratings ON ratings.movie_id = directors.movie_id
WHERE rating >= 9;
11. SELECT title FROM movies
JOIN ratings ON ratings.movie_id = movies.id
JOIN stars ON stars.movie_id = movies.id
WHERE stars.person_id =
(SELECT id FROM people WHERE name = 'Chadwick Boseman')
ORDER BY rating DESC
LIMIT 5;
12. SELECT title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE people.name = 'Bradley Cooper' AND people.name = 'Jennifer Lawrence';
13. SELECT name FROM people
    JOIN stars on people.id = stars.person_id
    JOIN movies on stars.movie_id = movies.id
    WHERE movies.id IN(
        SELECT movie_id FROM stars
        WHERE person_id = (SELECT id FROM people WHERE people.name = 'Kevin Bacon' AND people.birth = '1958')) AND name != 'Kevin Bacon';
