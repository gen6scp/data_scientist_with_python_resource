SELECT b.title, a.first_name, a.last_name
FROM books AS b
INNER JOIN authors AS a
USING (author_id);
