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

def main():
    aggregation()

if __name__ == "__main__":
    main()