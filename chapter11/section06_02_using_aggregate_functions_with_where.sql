-- Calculate the average price of books with Condition 1 and titles starting with 'H'
SELECT AVG(price) AS avg_price_H
FROM books
WHERE year_published < 2000 AND title LIKE 'H%';
