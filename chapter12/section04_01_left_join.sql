SELECT b.title, a.first_name, a.last_name
FROM books AS b
LEFT JOIN authors AS a
ON b.author_id = a.author_id;
