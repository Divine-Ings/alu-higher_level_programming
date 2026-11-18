# SQL_introduction

Introduction to SQL with MySQL: databases, tables, inserting, selecting,
updating, deleting, and simple aggregates.

## Requirements
- MySQL 8.0 (Ubuntu 20.04 LTS)
- All files end with a new line
- First line of every `.sql` file is a comment describing the script
- Scripts are run like this:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Files
| File | Description |
|------|-------------|
| 0-list_databases.sql | Lists all databases |
| 1-create_database_if_missing.sql | Creates `hbtn_0c_0` if missing |
| 2-remove_database.sql | Deletes `hbtn_0c_0` if it exists |
| 3-list_tables.sql | Lists the tables of a database |
| 4-first_table.sql | Creates `first_table` (`id INT`, `name VARCHAR(256)`) |
| 5-full_table.sql | Prints the full description of `first_table` |
| 6-list_values.sql | Lists all rows of `first_table` |
| 7-insert_value.sql | Inserts `(89, 'Best School')` into `first_table` |
| 8-count_89.sql | Counts the records with `id = 89` |
| 9-full_creation.sql | Creates `second_table` and inserts 4 rows |
| 10-top_score.sql | Lists score and name, top score first |
| 11-best_score.sql | Lists records with score >= 10 |
| 12-no_cheating.sql | Sets Bob's score to 10 (by name) |
| 13-change_class.sql | Deletes records with score <= 5 |
| 14-average.sql | Score average, column named `average` |
| 15-groups.sql | Number of records per score, labelled `number` |
| 16-no_link.sql | Lists score and name of rows that have a name |
