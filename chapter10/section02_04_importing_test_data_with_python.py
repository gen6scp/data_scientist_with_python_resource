import sqlite3

# Connect to SQLite (or create a new database if it doesn’t exist)
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Insert sample data into the books table
cursor.execute('''
    INSERT INTO books (title, author, genre, year_published, price)
    VALUES 
	('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 12.99),
	('1984', 'George Orwell', 'Science Fiction', 1949, 9.99),
	('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 7.99),
	('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 10.99),
	('Brave New World', 'Aldous Huxley', 'Science Fiction', 1932, 14.99),
	('Moby-Dick', 'Herman Melville', 'Adventure', 1851, 11.99),
	('Jane Eyre', 'Charlotte Brontë', 'Romance', 1847, 8.99),
	('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 1869, 13.99),
	('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 15.99),
	('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 9.49)
''')
conn.commit()

# Close the connection
conn.close()
