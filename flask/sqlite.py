import sqlite3 as sql

# create and connect to database
connection = sql.connect('data.db')

# cursor executes the query and stores the results
cursor = connection.cursor()


# to create table in db
print('[INFO] Creating table users')
createTable = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(createTable)


# to insert data into tables
user = (1, 'shubham', 'shubh123')

print('[INFO] inserting single value in db')
insertQuery = "INSERT INTO users values (?, ?, ?)"
cursor.execute(insertQuery, user)


# to insert multiple data

users = [
	(2, 'shubh', 'shubham123'),
	(3, 'am_shubh', '123shubh')
]

print('[INFO] inserting multiple values in db')
cursor.executemany(insertQuery, users)


# to fetch data from the db

print('[INFO] fetching data from db')
selectQuery = "SELECT * FROM users"		# or SELECT id, SELECT username...
for entries in cursor.execute(selectQuery):
	print(entries)


# to save data into the db
connection.commit()

# closing the connection
connection.close()