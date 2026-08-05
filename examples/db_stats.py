import sqlite3
from pathlib import Path


database_path = Path("pychronicle.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()


cursor.execute("SELECT COUNT(*) FROM execution_trace")
trace_count = cursor.fetchone()[0]


cursor.execute("SELECT SUM(LENGTH(locals_snapshot)) FROM execution_trace")
total_size = cursor.fetchone()[0] or 0

cursor.execute("SELECT AVG(LENGTH(locals_snapshot)) FROM execution_trace")
average_size = cursor.fetchone()[0] or 0