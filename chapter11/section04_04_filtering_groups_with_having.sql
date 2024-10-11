-- Find authors with an average book price greater than $12
SELECT author, AVG(price) AS average_price
FROM books
GROUP BY author
HAVING AVG(price) > 12;
