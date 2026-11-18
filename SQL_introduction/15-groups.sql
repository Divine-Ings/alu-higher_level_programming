-- Lists the number of records with the same score, biggest group first
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
