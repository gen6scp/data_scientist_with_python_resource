-- Round the price_in_euros to two decimal places
SELECT title, ROUND(price * 1.2, 2) AS price_in_euros
FROM books
LIMIT 20;
