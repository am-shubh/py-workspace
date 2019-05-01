from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.store import StoreModel

class Store(Resource):

	@classmethod
	def get(cls, name):
		store = StoreModel.find_by_name(name)

		if store:
			return store.json()

		return {'message': 'Store not found'}, 404

	@classmethod
	@jwt_required
	def post(cls, name):
		
		if StoreModel.find_by_name(name):
			return {'message': "A store with name '{}' already exists.".format(name)}, 400

		try:
			store = StoreModel(None, name)
			store.save_to_db()
		except:
			return {"message": "An error occured creating store"}, 500

		return store.json(), 201

	@classmethod
	@jwt_required
	def delete(cls,name):

		store = StoreModel.find_by_name(name)

		if store:
			store.delete_from_db()
			return {'message': 'Store Deleted'}

		return {"message": "store not found"}, 404


class StoreList(Resource):

	@classmethod
	def get(cls):

		stores = [store.json() for store in StoreModel.query.all()]

		responseData = {
			'count': len(stores),
			'stores': stores
		}

		return responseData
