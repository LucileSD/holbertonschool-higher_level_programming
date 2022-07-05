-- list the number of records with the sasme score
SELECT score, COUNT(*) as number FROM second_table
GROUP BY score
ORDER BY number DESC;
