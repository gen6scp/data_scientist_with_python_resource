-- Select titles and prices, sorted by price from highest to lowest
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 20;
