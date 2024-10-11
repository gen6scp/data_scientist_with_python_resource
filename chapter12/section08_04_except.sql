-- Colmun width adjustment (hacky!) 
.width 35 15 15 10

-- Find books that are not published by "Penguin Books" (publisher_id = 1)
SELECT title, publisher_id
FROM books
EXCEPT
SELECT title, publisher_id
FROM books
WHERE publisher_id = 1;
