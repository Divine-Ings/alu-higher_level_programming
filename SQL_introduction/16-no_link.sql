-- Lists score and name of records that have a name, top score first
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
