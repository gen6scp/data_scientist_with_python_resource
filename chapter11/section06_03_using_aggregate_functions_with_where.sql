-- Find the lowest priced book with Condition 2
SELECT MIN(price) AS lowest_price
FROM books
WHERE year_published < 2000 AND title LIKE 'H%';

