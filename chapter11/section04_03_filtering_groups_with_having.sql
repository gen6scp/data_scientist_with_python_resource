-- Find genres with more than 5 books
SELECT genre, COUNT(*) AS books_in_genre
FROM books
GROUP BY genre
HAVING COUNT(*) > 5;
