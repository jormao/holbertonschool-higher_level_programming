# SQL - Introduction

## Resources

### Read or watch
    What is Database & SQL?
    A Basic MySQL Tutorial
    Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
    Basic queries: SQL and RA
    SQL technique: functions
    SQL technique: subqueries
    What makes the big difference between a backtick and an apostrophe?
    MySQL Cheat Sheet
    MySQL 5.7 SQL Statement Syntax

## Learning Objectives


    What’s a database
    What’s a relational database
    What does SQL stand for
    What’s MySQL
    How to create a database in MySQL
    What does DDL and DML stand for
    How to CREATE or ALTER a table
    How to SELECT data from a table
    How to INSERT, UPDATE or DELETE data
    What are subqueries
    How to use MySQL functions

## Requirements


    Allowed editors: vi, vim, emacs
    All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

## More Info

### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

| TASKS | DESCRIPTION |
| ------ | ---------- |
| 0-list_databases.sql | script that lists all databases of your MySQL server.|
| 1-create_database_if_missing.sql | script that creates the database hbtn_0c_0 in your MySQL server.|
| 2-remove_database.sql | script that deletes the database hbtn_0c_0 in your MySQL server.|
| 3-list_tables.sql | script that lists all the tables of a database in your MySQL server.|
| 4-first_table.sql | script that creates a table called first_table in the current database in your MySQL server.|
| 5-full_table.sql | script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.|
| 6-list_values.sql | script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.|
| 7-insert_value.sql | script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.|
| 8-count_89.sql | script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.|
| 9-full_creation.sql | script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.|
| 10-top_score.sql | script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.|
| 11-best_score.sql | script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| 12-no_cheating.sql | script that updates the score of Bob to 10 in the table second_table.|
| 13-change_class.sql | script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| 14-average.sql | script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| 15-groups.sql | script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| 16-no_link.sql | script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.|
