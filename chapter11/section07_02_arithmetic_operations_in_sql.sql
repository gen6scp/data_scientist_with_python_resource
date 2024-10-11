-- Calculate the percentage of books priced over $10
SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM books)) AS percentage_over_10
FROM books
WHERE price > 10.00;
