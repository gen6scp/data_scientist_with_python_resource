-- Step 4: Order by average price descending
SELECT year_published, AVG(price) AS avg_price, COUNT(*) AS total_books
FROM books
WHERE year_published > 1980
GROUP BY year_published
HAVING AVG(price) > 12
ORDER BY avg_price DESC;
