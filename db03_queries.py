"""Python script to execute SQL queries from files."""

import sqlite3
import pathlib
import pandas as pd
from utils_logger import logger

db_file = pathlib.Path("project.sqlite3")  # Path to the SQLite database file

def execute_query(sql_file):
    """Execute a SQL query from a file."""
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
                statements = sql_script.split(";")
                queries = []
                for statement in statements:
                    if statement == "":
                        break
                    df = pd.read_sql_query(statement, conn)
                    queries.append(pd.DataFrame(df))
            logger.info(f"Query executed: {sql_file}")
    except sqlite3.Error as e:
        logger.error("Error executing query:", e)
    for q in queries:
        print(q)

def main():
    print("Aggregation")
    execute_query(pathlib.Path("sql_queries", "query_aggregation.sql"))
    print()
    print("Filter")
    execute_query(pathlib.Path("sql_queries", "query_filter.sql"))
    print()
    print("Sorting")
    execute_query(pathlib.Path("sql_queries", "query_sorting.sql"))
    print()
    print("Grouping")
    execute_query(pathlib.Path("sql_queries", "query_group_by.sql"))
    print()
    print("Join")
    execute_query(pathlib.Path("sql_queries", "query_join.sql"))

if __name__ == "__main__":
    main()