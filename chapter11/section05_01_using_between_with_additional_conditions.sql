-- Step 1: Select books published between 1995 and 2010 with price over $10
SELECT title, year_published, price, genre
FROM books
WHERE year_published BETWEEN 1995 AND 2010
  AND price > 10.00;
