# datafun-05-sql

This repository is for Project 5 of Data Analytics Fundamentals where we will be working with SQL

## How to Install and Run the Project

First you must clone the project to your local machine.

1. Copy the URL of the GitHub Repository you would like
2. Open Powershell and run the following commands

```shell
cd \
cd Projects
git clone https://github.com/**account**/**repo-name**
cd **repo-name**
code . 
```

If .gitignore and/or requirements.txt aren't created, create them.

After creating these files we can now Git add-commit-push using the following code in the terminal

```shell
git add . 
git commit -m "YOUR MESSAGE HERE"
git push -u origin main
```

Once pushed, we now create our virtual environment by running the command:

```shell
py -m venv .venv
```

Now we will activate the virtual environment using this command:

```shell
.venv\Scripts\activate
```

Once the virtual environment has been activated, we can install our dependencies from requirements.txt.

Before installing, it's best to update key packages first.

```shell
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

Lastly, we will select our VS Code Interpreter

1. Press Ctrl+Shift+P
2. Search for "Python: Select Interpreter"
3. Choose the Interpreter for the local .venv 

Now your project is ready and the real fun can begin

Don't forget to regularly Git add-commit-push to keep everything up to date




## Specifications of this Project

### Step 1. Schema Design and Database Initialization

Design a schema with at least two related tables, including foreign key constraints.
Document the schema design in your README.md.

sql_create folder:

- 01_drop_tables.sql - drop tables to restart
- 02_create_tables.sql - create your database schema using sql 
- 03_insert_records.sql - insert at least 10 additional records into each table.

db01_setup.py:

Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. 
Make it easy to re-run by dropping the tables first.




### Step 2. Cleaning and Feature Engineering

Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements.
You might create an additional table, insert new records,
and perform data querying (with filters, sorting, and joining tables),
data aggregation, and record update and deletion.

sql_features folder:

1. update_records.sql - update 1 or more records in a table.
2. delete_records.sql - delete 1 or more records from a table.

db02_features.py

Create a Python script that demonstrates the ability to run sql scripts 
to interact with fields, update records, delete records, and maybe add additional columns. 



### Step 3. Perform Aggregations and queries

Implement SQL statements and queries to perform aggregations and queries.

sql_queries folder: 

1. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
2. query_filter.sql - use WHERE to filter data based on conditions.
3. query_sorting.sql - use ORDER BY to sort data.
4. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
5. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

db03_queries.py



## Top Tools in SQL

1. SELECT and FROM Statement

The SELECT statement is the foundational tool for SQL for data analysis. It allows you to retrieve specific data from a database table, including specific columns, rows, or calculated values. TheFROM statement specifies the location or table from which the data needs to be retrieved.

2. WHERE Clause

The WHERE clause is used for filtering data. It allows you to specify conditions that the data must meet to be included in the query results. This is crucial for isolating relevant data.

3. GROUP BY Clause

The GROUP BY clause is used for data aggregation. It allows you to group rows with similar values in one or more columns and perform aggregate functions (e.g., SUM, AVG, COUNT) on those groups.

4. JOIN Operations

SQL supports different types of joins, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN, which enable you to combine data from multiple tables based on specified criteria.

5. ORDER BY Clause

The ORDER BY clause is used to sort query results in ascending or descending order based on one or more columns. It’s used for arranging data for analysis.

6. Mathematical and Statistical Functions

SQL provides a variety of built-in functions for performing mathematical and statistical calculations on data, such as SUM, AVG, MAX, MIN, STDDEV, and VARIANCE.

7. Date and Time Functions

SQL offers functions for handling date and time data, allowing for time-series analysis, date arithmetic, and formatting.

8. Subqueries

Subqueries, or nested queries, enable you to use the result of one query as input for another query. This is useful for complex data analysis tasks.

9. Data Modification Statements

SQL not only retrieves data but also allows you to modify data using statements like INSERT, UPDATE, and DELETE. This is important for data preparation and cleaning.

10. Window Functions

Window functions, like RANK(), LEAD(), and LAG(), are useful for performing calculations across rows within a specific window or partition of data.

11. Stored Procedures and User-Defined Functions (UDFs)

SQL databases often support the creation of stored procedures and user-defined functions. These can be used to encapsulate complex analysis logic for reuse.

12. Indexing

SQL databases provide indexing mechanisms to improve query performance, making data retrieval faster, which is crucial for large datasets.

13. Reporting Tools

Many SQL-based database management systems offer reporting and visualisation tools that allow you to create charts, graphs, and reports based on SQL query results.

## The Database

### The Tables

This project contains two related tables, one of which has a Foreign Key

- **authors** (table regarding the information about authors of novels)
    Features:
        - author_id
        - first
        - last
        - year_born

- **books** (table regarding the information about books)
    Features:
        - book_id
        - title
        - year_published
        - author_id (Foreign Key)
        - num_pages

### SQL Files

There are **three** SQL folders that, when combined, contain a total of **ten** SQL files.

- sql_create is a folder containing SQL files that are meant to create and fill tables
- sql_features is a folder containing SQL files that are meant to update tables
- sql_queries is a folder containing SQL files that are meant to perform tasks using information from the tables

Each SQL folder has a complementary Python file that runs the tasks for them.

### How to Run

It is imperative that the python scripts are executed in the correct order.

1. db01_setup.py (deletes any existing tables and creates and fills new ones)
    Correct Output:
    ![db01_setup.py output](https://github.com/DMill31/datafun-05-sql/blob/main/Screenshot%202025-02-13%20093538.png)
2. db02_features.py (alters these newly made tables with new features)
    Correct Output:
    ![db02_features.py output](https://github.com/DMill31/datafun-05-sql/blob/main/Screenshot%202025-02-13%20093600.png)
3. db03_queries.py (performs queries on the updated tables)
    Correct Output:
    ![db03_queries.py output](https://github.com/DMill31/datafun-05-sql/blob/main/Screenshot%202025-02-13%20093635.png)

Commands:
```shell
py db01_setup.py
py db02_features.py
py db03_queries.py
```