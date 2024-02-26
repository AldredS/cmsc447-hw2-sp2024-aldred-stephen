import sqlite3

connection = sqlite3.connect('database.db')

with open('makeTable.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Steve Smith', 211, 80))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Jian Wong', 122, 92))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Chris Peterson', 213, 91))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Sai Patel', 524, 94))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Andrew Whitehead', 425, 99))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Lynn Roberts', 626, 90))
cursor.execute("INSERT INTO data (user, id, points) VALUES (?, ?, ?)", ('Robert Sanders', 287, 75))

connection.commit()
connection.close()