import sqlite3
import pandas as pd

# Reconnect to the SQLite database to perform SQL queries
conn = sqlite3.connect('osint_data.db')

# Example Query 1: Count incidents by location
query1 = '''SELECT lat, lng, COUNT(*) AS incident_count
            FROM articles
            GROUP BY lat, lng
            ORDER BY incident_count DESC;'''
df_locations = pd.read_sql_query(query1, conn)
print("* Incidents by locations")
print(df_locations.head())

# Example Query 2: Find incidents between specific dates
query2 = '''SELECT * FROM articles
            WHERE Date BETWEEN '2023-10-01' AND '2024-10-01';'''
df_date_range = pd.read_sql_query(query2, conn)
print("\n* Incidents between specific dates")
print(df_date_range)

conn.close()
