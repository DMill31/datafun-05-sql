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