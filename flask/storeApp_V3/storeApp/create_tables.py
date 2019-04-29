import sqlite3 as sql

connection = sql.connect('data.db')
cursor = connection.cursor()

createUsersTable = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(createUsersTable)

createItemsTable = "CREATE TABLE IF NOT EXISTS items (_id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(createItemsTable)

connection.commit()
connection.close()