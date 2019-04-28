from flask import Flask, jsonify, request, render_template

PORT = 5500

app = Flask(__name__)

# store list
stores = [
	{
		'id': 0,
		'name': 'store1',
		'items': [
			{
				'name': 'item1',
				'price': 16.78
			}
		]
	},
	{
		'id': 1,
		'name': 'store2',
		'items': [
		]
	}
]

@app.route('/')
def index_page():
	return render_template('index.html')

# POST API to create the strore
@app.route('/store', methods=['POST'])
def create_store():
	requestData = request.get_json()

	newStore = {
		'id': requestData['id'],
		'name': requestData['name'],
		'items': []
	}

	stores.append(newStore)

	return jsonify({'new_store': newStore})


# GET API to get particular store
@app.route('/store/<string:storeId>')
def get_store(storeId):
	# iterate over all stores
	for store in stores:
		if store['id'] == int(storeId):
			return jsonify(store)

	# store is not found with given id
	return jsonify({'error': 'store not found'})


# GET API to get all stores
@app.route('/store')
def get_all_stores():
	return jsonify({'stores': stores})


# POST API to create item in store
@app.route('/store/<string:storeId>/item', methods=['POST'])
def create_item_in_store(storeId):

	requestData = request.get_json()

	# iterate over stores
	for store in stores:
		if store['id'] == int(storeId):

			newItem = {
				'name': requestData['name'],
				'price': requestData['price']
			}

			store['items'].append(newItem)

			return jsonify({'message': 'new item added', 'store': store})

	return jsonify({'error': 'store not found'})


# GET API to get items in store
@app.route('/store/<string:storeId>/item')
def get_items_in_store(storeId):
	# iterate over stores
	for store in stores:
		if store['id'] == int(storeId):
			if len(store['items']) > 0:
				return jsonify({'items': store['items']})

			else: 
				return jsonify({'message': 'store has 0 items'})

	return jsonify({'error': 'store not found'})


app.run(port=PORT)