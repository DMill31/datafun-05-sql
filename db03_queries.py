import sqlite3
import pathlib
import pandas as pd
from utils_logger import logger

db_file = pathlib.Path("project.sqlite3")  # Path to the SQLite database file

def aggregation():
    """Perform aggregation on the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
                statements = sql_script.split(";")
                aggregations = []
                for statement in statements:
                    if statement == "":
                        break
                    df = pd.read_sql_query(statement, conn)
                    logger.info(f"Aggreation performed: {statement}")
                    aggregations.append(pd.DataFrame(df))
            logger.info("All aggregations performed")
    except sqlite3.Error as e:
        logger.error("Error performing aggregation:", e)
    for a in aggregations:
        print(a)

def filter():
    """Perform filtering on the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
                statements = sql_script.split(";")
                filters = []
                for statement in statements:
                    if statement == "":
                        break
                    df = pd.read_sql_query(statement, conn)
                    logger.info(f"Filtering performed: {statement}")
                    filters.append(pd.DataFrame(df))
            logger.info("All filters performed")
    except sqlite3.Error as e:
        logger.error("Error performing filtering:", e)
    for f in filters:
        print(f)

def sorting():
    """Perform sorting on the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
                statements = sql_script.split(";")
                sorts = []
                for statement in statements:
                    if statement == "":
                        break
                    df = pd.read_sql_query(statement, conn)
                    logger.info(f"Sorting performed: {statement}")
                    sorts.append(pd.DataFrame(df))
            logger.info("All sorts performed")
    except sqlite3.Error as e:
        logger.error("Error performing sorting:", e)
    for s in sorts:
        print(s)

def grouping():
    """Perform grouping on the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_queries", "query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
                statements = sql_script.split(";")
                groups = []
                for statement in statements:
                    if statement == "":
                        break
                    df = pd.read_sql_query(statement, conn)
                    logger.info(f"Grouping performed: {statement}")
                    groups.append(pd.DataFrame(df))
            logger.info("All groups performed")
    except sqlite3.Error as e:
        logger.error("Error performing grouping:", e)
    for g in groups:
        print(g)

def main():
    aggregation()
    filter()
    sorting()
    grouping()

if __name__ == "__main__":
    main()