-- Find the number of books per genre
SELECT genre, COUNT(*) AS books_in_genre
FROM books
GROUP BY genre;
