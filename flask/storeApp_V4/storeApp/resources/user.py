from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
	create_access_token, 
	create_refresh_token, 
	jwt_refresh_token_required,
	get_jwt_identity,
	jwt_required,
	get_raw_jwt)
from models.user import UserModel
from blacklist import BLACKLIST

_userParser = reqparse.RequestParser()

_userParser.add_argument('username', type=str, required=True, help = 'username is required')
_userParser.add_argument('password', type=str, required=True, help = 'password is required')


class UserRegister(Resource):

	@classmethod
	def post(cls):

		requestData = _userParser.parse_args()

		if UserModel.find_by_username(requestData['username']):
			return {"message": "User already exists"}, 400

		try:

			user = UserModel(None, **requestData)

			user.save_to_db()

			return {"message": "User created successfully."}, 201

		except:

			return {"message": "Could not Save user"}, 500


class User(Resource):

	@classmethod
	def get(cls, userId):
		user = UserModel.find_by_id(userId)
		if user:
			return user.json()

		return {'message': 'User not Found'}, 404


	@classmethod
	def delete(cls, userId):
		user = UserModel.find_by_id(userId)
		if user:
			user.delete_from_db()
			return {'message': 'User deleted'}

		return {'message': 'User not Found'}, 404


class UserLogin(Resource):

	@classmethod
	def post(cls):

		# get data from request parser
		requestData = _userParser.parse_args()

		# find user in database

		user = UserModel.find_by_username(requestData['username'])

		# check password

		if user and safe_str_cmp(user.password, requestData['password']):
			# create access token
			access_token = create_access_token(identity=user.id, fresh=True)

			# create refresh token
			refresh_token = create_refresh_token(user.id)

			return {
				'access_token': access_token,
				'refresh_token': refresh_token
			}, 200

		return {'message': 'Invalid credentials'}, 401


class UserLogout(Resource):

	@classmethod
	@jwt_required
	def post(cls):
		jti = get_raw_jwt()['jti']
		BLACKLIST.add(jti)

		return {'message': 'successfully logged out'}, 200



class TokenRefresh(Resource):

	@classmethod
	@jwt_refresh_token_required
	def post(cls):
		currentUser = get_jwt_identity()
		new_token = create_access_token(identity=currentUser, fresh=False)
		return {'access_token': new_token}, 200


