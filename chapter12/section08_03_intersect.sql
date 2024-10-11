-- Colmun width adjustment (hacky!) 
.width 10 10 10 10

-- Find author IDs that appear in both the authors and books table and display their first_name and last_name
SELECT author_id, first_name, last_name
FROM authors
WHERE author_id IN (
    SELECT author_id FROM authors
    INTERSECT
    SELECT author_id FROM books
);
