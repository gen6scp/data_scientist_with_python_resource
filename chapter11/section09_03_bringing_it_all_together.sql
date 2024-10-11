-- Step 3: Filter for years with an average price over $12
SELECT year_published, AVG(price) AS avg_price, COUNT(*) AS total_books
FROM books
WHERE year_published > 1980
GROUP BY year_published
HAVING AVG(price) > 12;
