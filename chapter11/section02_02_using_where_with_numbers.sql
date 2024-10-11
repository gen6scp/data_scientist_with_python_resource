-- Select titles and authors of books published before 1980
SELECT title, author
FROM books
WHERE year_published < 1980 LIMIT 10;
