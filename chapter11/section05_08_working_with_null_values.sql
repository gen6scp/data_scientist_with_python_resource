-- List all book titles with missing prices
SELECT title
FROM books
WHERE price IS NULL;
