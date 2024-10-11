-- Count unique titles for Thriller books published between 1990 and 2010 and priced below $20
SELECT COUNT(DISTINCT title) AS thriller_books
FROM books
WHERE year_published BETWEEN 1990 AND 2010
  AND genre = 'Thriller'
  AND price < 20.00;
