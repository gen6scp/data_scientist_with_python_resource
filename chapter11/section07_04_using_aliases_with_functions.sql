-- Calculate the number of decades represented in the books table
SELECT ((MAX(year_published) - MIN(year_published)) / 10) AS number_of_decades
FROM books;
