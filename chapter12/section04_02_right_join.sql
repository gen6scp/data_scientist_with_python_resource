SELECT a.first_name, a.last_name, b.title
FROM authors AS a
RIGHT JOIN books AS b
ON a.author_id = b.author_id;
