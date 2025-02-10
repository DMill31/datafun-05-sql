import sqlite3
import pandas as pd
import pathlib
from utils_logger import logger

db_file = pathlib.Path("project.sqlite3")

def create_db():
    """Create a new SQLite database. If the file doesn't exist, it will be created.
    Close the connection to the database when done."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        logger.info(f"Database created: {db_file}")
    except sqlite3.Error as e:
        logger.error("Error creating database:", e)

def drop_tables():
    """Function that reads and executes SQL statements to drop tables."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "01_drop_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables dropped")
    except sqlite3.Error as e:
        logger.error("Error dropping tables:", e)


def create_tables():
    """Read and execute SQL statements to create tables."""
    # Drop tables first
    drop_tables()
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "02_create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables created")
    except sqlite3.Error as e:
        logger.error("Error creating tables:", e)

def main():
    create_db()
    create_tables()

if __name__ == "__main__":
    main()