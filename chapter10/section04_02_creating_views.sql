-- Drop (Remove) a fiction_books view if it exists
DROP VIEW IF EXISTS fiction_books;

-- Create a view that contains all Fiction books
CREATE VIEW fiction_books AS
SELECT * FROM books WHERE genre = 'Fiction';

-- Query the view
SELECT * FROM fiction_books;
