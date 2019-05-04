import traceback
from flask_restful import Resource
from flask import request, make_response, render_template
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
	create_access_token,
	jwt_required,
	get_jwt_claims)

from marshmallow import ValidationError
from models.user import UserModel
from schemas.user import UserSchema
from libs.mailgun import MailGunException

user_schema = UserSchema()

class UserRegister(Resource):

	@classmethod
	def post(cls):

		try:
			user = user_schema.load(request.get_json())
		except ValidationError as err:
			return err.messages, 400

		if UserModel.find_by_username(user.username):
			return {"message": "User already exists"}, 400

		if UserModel.find_by_email(user.email):
			return {"message": "Email already exists"}, 400

		try:
			user.save_to_db()
			user.send_confirmation_email()
			return {"message": "Account created successfully.. An email with activation link has been sent to your email"}, 201

		except MailGunException as e:
			user.delete_from_db()
			return {"message": str(e)}, 500

		except:
			traceback.print_exc()
			return {"message": "Could not Save user"}, 500


class User(Resource):

	@classmethod
	@jwt_required
	def get(cls, userId):
		claims = get_jwt_claims()

		if not claims['is_admin']:
			return {'message': 'Admin privilege required'}, 401

		user = UserModel.find_by_id(userId)
		if user:
			return user_schema.dump(user), 200

		return {'message': 'User not Found'}, 404

	@classmethod
	@jwt_required
	def delete(cls, userId):

		if userId == 1:
			return {'message': 'Can not delete super admin'}, 401
			
		claims = get_jwt_claims()

		if not claims['is_admin']:
			return {'message': 'Admin privilege required'}, 401

		user = UserModel.find_by_id(userId)
		if user:
			user.delete_from_db()
			return {'message': 'User deleted'}

		return {'message': 'User not Found'}, 404


class UserLogin(Resource):

	@classmethod
	def post(cls):

		try:
			userData = user_schema.load(request.get_json(), partial=("email",))
		except ValidationError as err:
			return err.messages, 400

		# find user in database
		user = UserModel.find_by_username(userData.username)

		# check password

		if user and safe_str_cmp(user.password, userData.password):
			
			if user.activated:
				# create access token
				access_token = create_access_token(identity=user.id)

				return {
					'access_token': access_token
				}, 200

			# if user not activated, return message
			else:
				return {'message': 'your email: {} is not confirmed'.format(user.email)}, 400

		return {'message': 'Invalid credentials'}, 401


class ConfirmUser(Resource):

	@classmethod
	def get(cls, userId: int):

		headers = {"Content-Type": "text/html"}

		# get user from database
		user = UserModel.find_by_id(userId)

		if user:
			# check for activated field. if not activated, activate the user
			if not user.activated:
				# save the user to database with updated fields
				user.activated = True
				user.save_to_db()

				# return message
				return make_response(render_template("confirmation_page.html", message = "Your registration is confirmed through {}".format(user.email)), 200, headers)

			return make_response(render_template("confirmation_page.html", message = "Your registration is already confirmed through {}".format(user.email)), 400, headers)

		return make_response(render_template("error_page.html", message = "You are not registered"), 401, headers)



