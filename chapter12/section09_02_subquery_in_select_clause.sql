-- Colmun width adjustment (hacky!) 
.width 15 15 10 10 10 10 

SELECT a.first_name, a.last_name,
    (SELECT COUNT(*)
     FROM books AS b
     WHERE b.author_id = a.author_id) AS book_count
FROM authors AS a;
