import sqlite3

connection = sqlite3.connect('chinook.db')

cursor = connection.execute("Select firstname,email from Customers;")
for row in cursor:
    print(row[0], row[1])

connection.close()
