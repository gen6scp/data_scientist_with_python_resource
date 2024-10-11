-- Count the number of books published after 1990
SELECT COUNT(*) AS books_after_1990
FROM books
WHERE year_published > 1990;
