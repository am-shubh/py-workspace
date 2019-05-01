from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from resources.items import Item, Items
from resources.store import Store, StoreList
from blacklist import BLACKLIST

PORT = 5500

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = '3ec8eY-$et'

api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_token_blacklisted(decryptedToken):
	return decryptedToken['jti'] in BLACKLIST


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

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
	return jsonify({
			'message': 'token is not fresh',
			'error': 'fresh_token_required'
		}), 401

@jwt.revoked_token_loader
def revoked_token_callback():
	return jsonify({
			'message': 'token has been revoked',
			'error': 'token_revoked'
		}), 401


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:userId>')
api.add_resource(UserLogin, '/auth')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogout, '/logout')
api.add_resource(Item, '/item/<int:_id>', '/item')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port = PORT, debug=True)