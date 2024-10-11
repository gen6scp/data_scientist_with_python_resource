-- Calculate the discounted price (10% off)
SELECT title, price, ROUND((price * 0.9), 2) AS discounted
FROM books
LIMIT 20;
