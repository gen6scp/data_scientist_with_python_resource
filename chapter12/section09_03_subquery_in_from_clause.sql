SELECT p.name AS publisher, avg_sales
FROM publishers AS p
INNER JOIN (
    SELECT publisher_id, AVG(sales) AS avg_sales
    FROM books
    GROUP BY publisher_id
) AS sub
ON p.publisher_id = sub.publisher_id;
