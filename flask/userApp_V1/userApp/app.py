import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import (
	UserRegister, 
	User, 
	UserLogin, 
	ConfirmUser)

from ma import ma
from db import db

PORT = 5500

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get("SECRET_KEY")

api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
	if identity == 1:
		return {'is_admin': True}
	return {'is_admin': False}

@jwt.expired_token_loader
def expired_token_callback():
	return jsonify({
			'message': 'The token has expired.',
			'error': 'token_expired'
		}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
	return jsonify({
			'message': 'signature verification failed',
			'error': 'invalid_token'
		}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
	return jsonify({
			'message': 'Request does not contain access token',
			'error': 'authorization_required'
		}), 401


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:userId>')
api.add_resource(UserLogin, '/auth')
api.add_resource(ConfirmUser, '/confirm_user/<int:userId>')


if __name__ == '__main__':
	db.init_app(app)
	ma.init_app(app)
	app.run(port = PORT, debug=True)