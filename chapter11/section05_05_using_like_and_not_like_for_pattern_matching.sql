-- Select titles that do not start with 'A', 'T' 'G', or 'C'
SELECT title
FROM books
WHERE title NOT LIKE 'A%' AND title NOT LIKE 'T%'
AND title NOT LIKE 'G%' AND title NOT LIKE 'C%';
