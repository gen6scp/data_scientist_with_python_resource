-- Drop (Remove) a publishers table if it exists
DROP TABLE IF EXISTS publishers;

-- Create the publishers table 
CREATE TABLE IF NOT EXISTS publishers (
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

