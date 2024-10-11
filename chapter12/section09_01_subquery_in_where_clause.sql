SELECT title, sales
FROM books
WHERE sales > (
    SELECT AVG(sales)
    FROM books
);
