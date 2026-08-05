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

print("PyChronicle Database Statistics")
print("-" * 40)
print(f"Total Trace Records : {trace_count}")
print(f"Total Snapshot Size : {total_size} bytes")
print(f"Average Delta Size  : {average_size:.2f} bytes")

connection.close()