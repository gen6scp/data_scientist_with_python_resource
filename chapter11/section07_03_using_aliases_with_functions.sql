-- Calculate the price in euros and alias the column
SELECT title, (price * 1.2) AS price_in_euros
FROM books
LIMIT 20;
