-- Drop (Remove) a authors table if it exists
DROP TABLE IF EXISTS authors;

-- Create the authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
