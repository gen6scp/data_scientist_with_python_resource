SELECT date, COUNT(*) AS incident_count
FROM articles
GROUP BY date
ORDER BY incident_count DESC
LIMIT 20;
