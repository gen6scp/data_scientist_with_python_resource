-- Count how many books exist in each genre
SELECT genre, COUNT(*) FROM books GROUP BY genre;
