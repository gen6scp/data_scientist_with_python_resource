import sqlite3

# Connect to SQLite (or create a new database if it doesn’t exist)
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Print the cursor object
print(cursor)
