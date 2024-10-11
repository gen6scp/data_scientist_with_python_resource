-- Find the maximum price per genre per year
SELECT genre, year_published, MAX(price) AS max_price
FROM books
GROUP BY genre, year_published
ORDER BY year_published, genre
LIMIT 20;
