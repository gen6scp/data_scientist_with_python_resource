-- Calculate the total price of books published before 2000
SELECT SUM(price) AS total_price
FROM books
WHERE year_published < 2000;
