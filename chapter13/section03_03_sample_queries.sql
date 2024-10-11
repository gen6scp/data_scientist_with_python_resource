SELECT lat, lng, COUNT(*) AS num_incidents
FROM articles
GROUP BY lat,lng
ORDER BY num_incidents DESC
LIMIT 20;
