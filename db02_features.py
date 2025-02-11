import sqlite3
import pathlib
from utils_logger import logger

db_file = pathlib.Path("project.sqlite3")  # Path to the SQLite database file

def update_db():
    """Update the database with new features."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Database updated")
    except sqlite3.Error as e:
        logger.error("Error updating database:", e)


def delete_db():
    """Delete a record from the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Record deleted")
    except sqlite3.Error as e:
        logger.error("Error deleting record:", e)


def main():
    update_db()
    delete_db()

if __name__ == "__main__":
    main()