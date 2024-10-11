-- Find books by specific authors
SELECT title, author
FROM books
WHERE author IN ('George Orwell', 'Harper Lee', 'Jane Austen');
