-- Colmun width adjustment (hacky!) 
.width 15 15 15 10

SELECT SUM(b.sales) AS total_sales, a.first_name, a.last_name 
FROM authors AS a
INNER JOIN books AS b
ON a.author_id = b.author_id
GROUP BY a.author_id, a.first_name, a.last_name
HAVING SUM(b.sales) > 500000;
