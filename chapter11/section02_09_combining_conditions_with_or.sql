-- Select books written by 'George Orwell' or 'Aldous Huxley'
SELECT title
FROM books
WHERE author = 'George Orwell' OR author = 'Aldous Huxley';
