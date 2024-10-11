-- Select books written by 'Jane Austen' and published before 1900
SELECT title
FROM books
WHERE author = 'Jane Austen' AND year_published < 1900;
