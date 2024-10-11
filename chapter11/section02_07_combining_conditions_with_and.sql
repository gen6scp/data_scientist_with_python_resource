-- Select 'Science Fiction' books published after 1950
SELECT title
FROM books
WHERE genre = 'Science Fiction' AND year_published > 1950;
