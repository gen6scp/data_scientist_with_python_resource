-- Find the year with the most books published in the Fiction genre
SELECT year_published, COUNT(*) AS fiction_books_count
FROM books
WHERE genre = 'Fiction'
GROUP BY year_published
ORDER BY fiction_books_count DESC
LIMIT 1;
