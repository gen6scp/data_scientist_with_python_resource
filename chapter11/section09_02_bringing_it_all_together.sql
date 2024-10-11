-- Step 2: Include average price and count of books
SELECT year_published, AVG(price) AS avg_price, COUNT(*) AS total_books
FROM books
WHERE year_published > 1980
GROUP BY year_published;
