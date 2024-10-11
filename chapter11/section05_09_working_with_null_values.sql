-- Count the number of books with known genres
SELECT COUNT(*) AS books_with_genre
FROM books
WHERE genre IS NOT NULL;
