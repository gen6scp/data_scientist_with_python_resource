-- Colmun width adjustment (hacky!) 
.width 35 35 10 10 10 10 

SELECT b1.title AS book, b2.title AS series
FROM books AS b1
LEFT JOIN books AS b2
ON b1.author_id = b2.author_id
AND b1.book_id != b2.book_id;

