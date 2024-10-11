-- Width
.width 10 10 45

SELECT date, post_id, text 
FROM articles
WHERE Date BETWEEN '2024-10-01' AND '2024-10-05'
LIMIT 20;
