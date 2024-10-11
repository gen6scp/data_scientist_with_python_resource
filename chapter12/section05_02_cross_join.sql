SELECT b.title, a.first_name, a.last_name
FROM authors AS a
CROSS JOIN books AS b
LIMIT 50;
