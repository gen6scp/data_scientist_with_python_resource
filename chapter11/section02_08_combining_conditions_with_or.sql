-- Select books published in either 1990 or 2000
SELECT title, year_published
FROM books
WHERE year_published = 1990 OR year_published = 2000;
