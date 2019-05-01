import sqlite3 as sql
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('username', type=str, required=True, help = 'username is required')
	parser.add_argument('password', type=str, required=True, help = 'password is required')

	def post(self):

		requestData = UserRegister.parser.parse_args()

		if UserModel.find_by_username(requestData['username']):
			return {"message": "User already exists"}, 400

		try:

			user = UserModel(None, **requestData)

			user.save_to_db()

			return {"message": "User created successfully."}, 201

		except:

			return {"message": "Could not Save user"}, 500


