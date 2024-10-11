SELECT b.title, a.first_name, a.last_name, p.name AS publisher
FROM books AS b
INNER JOIN authors AS a
ON b.author_id = a.author_id
INNER JOIN publishers AS p
ON b.publisher_id = p.publisher_id;
