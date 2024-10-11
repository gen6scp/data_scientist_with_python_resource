import sqlite3

# Connect to SQLite (or create a new database if it doesn’t exist)
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Drop (Remove) a books table if it exists
cursor.execute('''
   DROP TABLE IF EXISTS books
''')

# Create the books table with columns for ID, title, author, genre, year_published, and price
cursor.execute('''
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    year_published INTEGER,
    price REAL
  )
''')
conn.commit()
