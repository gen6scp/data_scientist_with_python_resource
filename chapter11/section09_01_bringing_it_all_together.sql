-- Step 1: Select years after 1980 and group by year_published
SELECT year_published
FROM books
GROUP BY year_published
HAVING year_published > 1980;
