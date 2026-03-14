-- Lists the number of records with the same score in the table second_table.
-- Displays the score and the number of records for that score with the label 'number'.
-- The list is sorted by the number of records in descending order.
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
