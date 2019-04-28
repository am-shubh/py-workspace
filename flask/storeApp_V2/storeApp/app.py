from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

PORT = 5500

app = Flask(__name__)
app.secret_key = '3ec8eY-$et'

api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('name', type=str, required=True, help = 'name is required')
	parser.add_argument('price', type=float, required=True, help = 'price is required')


	def get(self,_id):

		item = next(filter(lambda x: x['_id'] == _id, items), None)

		return {'item': item}, 200 if item else 404

	@jwt_required()
	def post(self):

		requestData = Item.parser.parse_args()

		item = next(filter(lambda x: x['name'] == requestData['name'], items), None)

		if item:

			return {'message': 'item name already exists'}, 409

		else:

			newItem = {
				'_id': len(items) + 1,
				'name': requestData['name'],
				'price': requestData['price']
			}

			items.append(newItem)

			responseData = {
				'message': 'item created successfully with id '+ str(newItem['_id']),
				'items': items
			}

			return responseData, 201


	@jwt_required()
	def delete(self, _id):
		global items
		items = list(filter(lambda x: x['_id'] != _id, items))

		return {'message': 'Item Deleted'}

	
	@jwt_required()
	def put(self, _id):

		requestData = Item.parser.parse_args()

		item = next(filter(lambda x: x['_id'] == _id, items), None)

		if item is None:

			item = {
				'_id': len(items) + 1,
				'name': requestData['name'],
				'price': requestData['price']
			}

			items.append(item)
			message = 'item created'

		else:

			item.update(requestData)
			message = 'item updated'

		responseData = {
			'message': message,
			'item': item
		}

		return responseData



class Items(Resource):

	def get(self):

		responseData = {
			'count': len(items),
			'items': items
		}

		return responseData


api.add_resource(Item, '/item/<int:_id>', '/item')
api.add_resource(Items, '/items')

app.run(port = PORT, debug=True)