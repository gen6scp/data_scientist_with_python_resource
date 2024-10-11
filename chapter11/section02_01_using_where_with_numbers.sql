-- Select books published after the year 2000
SELECT title, year_published
FROM books
WHERE year_published > 2000 LIMIT 10;
