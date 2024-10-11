-- Select the top 3 most expensive books
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 3;
