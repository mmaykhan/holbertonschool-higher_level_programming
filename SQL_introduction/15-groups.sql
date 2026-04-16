-- Lists the number of records with the same score
-- Display score and the number of records with label number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
