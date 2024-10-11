-- Insert a new book into the table
INSERT INTO books (title, author, genre)
VALUES ('Flying Saucers Have Landed', 'George Adamski', 'Ufology');

-- Get books by Adamski
SELECT * FROM books WHERE author ='George Adamski';
