-- Calculate the average price rounded to the nearest ten
SELECT ROUND(AVG(price), -1) AS avg_price_nearest_ten
FROM books;
