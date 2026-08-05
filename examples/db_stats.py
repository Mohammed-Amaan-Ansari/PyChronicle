import sqlite3
from pathlib import Path


database_path = Path("pychronicle.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()