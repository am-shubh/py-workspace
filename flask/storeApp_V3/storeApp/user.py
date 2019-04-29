import sqlite3 as sql
from flask_restful import Resource, reqparse

class User:

	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

	
	@classmethod
	def find_by_username(cls, username):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE username=?"

		result = cursor.execute(query, (username,))

		row = result.fetchone()

		if row:
			user = cls(*row)
		else:
			user = None

		connection.close()
		return user

	
	@classmethod
	def find_by_id(cls, _id):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE id=?"

		result = cursor.execute(query, (_id,))

		row = result.fetchone()

		if row:
			user = cls(*row)
		else:
			user = None

		connection.close()
		return user



class UserRegister(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('username', type=str, required=True, help = 'username is required')
	parser.add_argument('password', type=str, required=True, help = 'password is required')

	def post(self):

		requestData = UserRegister.parser.parse_args()

		if User.find_by_username(requestData['username']):
			return {"message": "User already exists"}, 400

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO users VALUES (NULL, ?, ?)"

		cursor.execute(query, (requestData['username'], requestData['password']))

		connection.commit()
		connection.close()

		return {"message": "User created successfully."}, 201


