-- list all records of the table
SELECT score, name FROM second_table
WHERE LENGTH(name) > 0
ORDER BY score DESC;
