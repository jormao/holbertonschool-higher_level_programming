# SQL - More queries 

## Resources

### Read or watch:


    How To Create a New User and Grant Permissions in MySQL
    How To Use MySQL GRANT Statement To Grant Privileges To a User
    MySQL constraints
    SQL technique: subqueries
    Basic query operation: the join
    SQL technique: multiple joins and the distinct keyword
    SQL technique: join types
    SQL technique: union and minus
    MySQL Cheat Sheet
    The Seven Types of SQL Joins
    MySQL Tutorial
    SQL Style Guide
    MySQL 5.7 SQL Statement Syntax

## Learning Objectives


    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What’s a PRIMARY KEY
    What’s a FOREIGN KEY
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What are subqueries
    What are JOIN and UNION

## Requirements


    Allowed editors: vi, vim, emacs
    All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
    All your files should end with a new line
    All your SQL queries should have a comment just before (i.e. syntax above)
    All your files should start by a comment describing the task
    All SQL keywords should be in uppercase (SELECT, WHERE…)
    A README.md file, at the root of the folder of the project, is mandatory
    The length of your files will be tested using wc

| TASKS | DESCRIPTION |
| ------- | --------- |
| 0-privileges.sql | script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost) |
| 1-create_user.sql |  script that creates the MySQL server user user_0d_1 |
| 2-create_read_user.sql | script that creates the database hbtn_0d_2 and the user user_0d_2 |
| 3-force_name.sql | script that creates the table force_name on your MySQL server.|
| 4-never_empty.sql | script that creates the table id_not_null on your MySQL server.|
| 5-unique_id.sql | script that creates the table unique_id on your MySQL server. |
| 6-states.sql | script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.|
| 7-cities.sql | script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.|
| 8-cities_of_california_subquery.sql | script that lists all the cities of California that can be found in the database hbtn_0d_usa | 
| 9-cities_by_state_join.sql | script that lists all cities contained in the database hbtn_0d_usa |
| 10-genre_id_by_show.sql | script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked |
| 11-genre_id_all_shows.sql | script that lists all shows contained in the database hbtn_0d_tvshows | 
| 12-no_genre.sql | script that lists all shows contained in hbtn_0d_tvshows without a genre linked | 
| 13-count_shows_by_genre.sql | script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each |
