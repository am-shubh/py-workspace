from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required

from models.items import ItemModel

class Item(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('name', type=str, required=True, help = 'name is required')
	parser.add_argument('price', type=float, required=True, help = 'price is required')
	parser.add_argument('store_id', type=int, required=True, help = 'store Id is required')


	def get(self,_id):

		item = ItemModel.findItem(_id = _id)

		if item:
			return item.json()

		return {"message": "item not found"}, 404

	
	@jwt_required
	def post(self):

		requestData = Item.parser.parse_args()

		if ItemModel.findItem(name = requestData['name']):
			return {'message': 'item name already exists'}, 400			

		try:
			item = ItemModel(None, **requestData)
			item.save_to_db()

		except:
			return {"message": "An error occured inserting the item"}, 500

		created_item = ItemModel.findItem(name = requestData['name'])

		return {"message": "item created successfully.", "item": created_item.json()}, 201


	@jwt_required
	def delete(self, _id):

		item = ItemModel.findItem(_id = _id)

		if item:
			item.delete_from_db()
			return {'message': 'Item Deleted'}

		return {"message": "item not found"}, 404

	
	@jwt_required
	def put(self, _id):

		requestData = Item.parser.parse_args()

		item = ItemModel.findItem(_id = _id)

		if item:

			try:

				item.name = requestData['name']
				item.price = requestData['price']
				item.store_id = requestData['store_id']

				item.save_to_db()

			except:
				return {"message": "An error occured updating the item"}, 500


			responseData = {
				"message": 'Item Updated',
				"item": item.json()
			}

			return responseData

		else:
			return {"message": "Item does not exists"}, 404


class Items(Resource):

	def get(self):

		items = [item.json() for item in ItemModel.query.all()]

		responseData = {
			'count': len(items),
			'items': items
		}

		return responseData
