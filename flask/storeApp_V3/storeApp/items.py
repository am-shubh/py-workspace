from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
import sqlite3 as sql

class Item(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('name', type=str, required=True, help = 'name is required')
	parser.add_argument('price', type=float, required=True, help = 'price is required')


	def get(self,_id):

		item = self.findItem(_id = _id)

		if item:
			return item

		return {"message": "item not found"}, 404


	@classmethod
	def findItem(cls, **kwargs):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		for key, value in kwargs.items():
			item = key
			itemValue = value

		if(item == '_id'):
			query = "SELECT * FROM items WHERE _id=?"
		else:
			query = "SELECT * FROM items WHERE name=?"

		result = cursor.execute(query, (itemValue,))
		row = result.fetchone()
		connection.close()

		if row:
			return {'_id': row[0], 'name': row[1], 'price': row[2]}


	@classmethod
	def insertItem(cls, *args):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES (NULL, ?, ?)"

		cursor.execute(query, (args[0], args[1]))

		connection.commit()
		connection.close()

	@classmethod
	def updateItem(cls, *args):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "UPDATE items SET name=?, price=? WHERE _id=?"

		cursor.execute(query, (args[1], args[2], args[0]))

		connection.commit()
		connection.close()

	
	@jwt_required()
	def post(self):

		requestData = Item.parser.parse_args()

		if self.findItem(name = requestData['name']):
			return {'message': 'item name already exists'}, 400			

		try:
			self.insertItem(requestData['name'], requestData['price'])
		except:
			return {"message": "An error occured inserting the item"}, 500

		item = self.findItem(name = requestData['name'])

		return {"message": "item created successfully.", "item": item}, 201

		# responseData = {
		# 	'message': 'item created successfully with id '+ str(newItem['_id']),
		# 	'items': items
		# }

		# return responseData, 201


	@jwt_required()
	def delete(self, _id):
		
		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "DELETE FROM items WHERE _id=?"

		cursor.execute(query, (_id,))

		connection.commit()
		connection.close()

		return {'message': 'Item Deleted'}

	
	@jwt_required()
	def put(self, _id):

		requestData = Item.parser.parse_args()

		item = self.findItem(_id = _id)

		if item is None:
			
			return {"message": "Item does not exists"}, 400

		else:
			try:

				self.updateItem(_id, requestData['name'], requestData['price'])
				message = 'item updated'

			except:
				return {"message": "An error occured updating the item"}, 500


			responseData = {
				"message": message,
				"item": {
					"_id": _id,
					"name": requestData['name'],
					"price": requestData['price']
				}
			}

			return responseData
	



class Items(Resource):

	def get(self):

		connection = sql.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM items"

		result = cursor.execute(query)

		items = []

		for row in result:
			items.append({"_id":row[0], "name":row[1], "price":row[2]})

		connection.commit()
		connection.close()

		responseData = {
			'count': len(items),
			'items': items
		}

		return responseData
