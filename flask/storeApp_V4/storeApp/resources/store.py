from flask_restful import Resource
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity

from models.store import StoreModel

class Store(Resource):

	def get(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return store.json()

		return {'message': 'Store not found'}, 404

	@jwt_required
	def post(self, name):
		
		if StoreModel.find_by_name(name):
			return {'message': "A store with name '{}' already exists.".format(name)}, 400

		try:
			store = StoreModel(None, name)
			store.save_to_db()
		except:
			return {"message": "An error occured creating store"}, 500

		return store.json(), 201

	@jwt_required
	def delete(self,name):

		store = StoreModel.find_by_name(name)

		if store:
			store.delete_from_db()
			return {'message': 'Store Deleted'}

		return {"message": "store not found"}, 404


class StoreList(Resource):

	@jwt_optional
	def get(self):

		user_id = get_jwt_identity()

		stores = [store.json() for store in StoreModel.query.all()]

		if user_id:

			responseData = {
				'count': len(stores),
				'stores': stores
			}

			return responseData

		return {
			'stores': [store['name'] for store in stores],
			'message': 'More data available if you log in'
		}, 200
