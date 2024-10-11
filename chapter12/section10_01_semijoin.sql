-- Colmun width adjustment (hacky!) 
.width 15 15 10 10 10 10 

SELECT first_name, last_name
FROM authors AS a
WHERE EXISTS (
    SELECT 1
    FROM books AS b
    WHERE b.author_id = a.author_id AND b.sales > 600000
);
