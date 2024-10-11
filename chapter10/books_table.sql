-- Drop (Remove) a books table if it exists
DROP TABLE IF EXISTS books;

-- Create the books table with columns for ID, title, author, genre, year_published, and price
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    year_published INTEGER,
    price REAL
);

