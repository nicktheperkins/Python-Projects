import sqlite3

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
