-- Update all Ufology books to a new genre label
UPDATE books SET genre = 'Adventure' WHERE genre = 'Ufology';

-- Get books by Adamski
SELECT * FROM books WHERE author ='George Adamski';

