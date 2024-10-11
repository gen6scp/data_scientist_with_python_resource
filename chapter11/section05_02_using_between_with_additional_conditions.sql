-- Step 2: Further narrow down the query to include only Thriller books
SELECT title, year_published, price, genre
FROM books
WHERE year_published BETWEEN 1995 AND 2010
  AND price > 10.00
  AND genre = 'Thriller';
