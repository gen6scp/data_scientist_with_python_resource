-- Sort by year_published, then by price
SELECT title, year_published, price
FROM books
ORDER BY year_published, price
LIMIT 20;
