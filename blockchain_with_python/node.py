from flask import Flask, jsonify, request
from flask_cors import CORS

from wallet import Wallet
from blockchain import Blockchain

PORT = 5000

app = Flask(__name__)
wallet = Wallet()
blockchain = None
CORS(app)


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
	chain = blockchain.get_chain()
	chain_dict = [block.__dict__.copy() for block in chain]
	for eachChain in chain_dict:
		eachChain['transactions'] = [tx.__dict__ for tx in eachChain['transactions']]
	
	return jsonify(chain_dict), 200


@app.route('/mine', methods=['POST'])
def mine():

	block = blockchain.mine_block()

	if block != None:

		block_dict = block.__dict__.copy()
		block_dict['transactions'] = [tx.__dict__ for tx in block_dict['transactions']]

		response = {
			'message': 'Block mined and added to blockchain',
			'block': block_dict
		}

		return jsonify(response), 200
		
	else:
		response = {
			'message': 'Mining Failed',
			'wallet_set_up': wallet.public_key != None
		}
		return jsonify(response), 500


@app.route('/public_key', methods=['GET'])
def get_public_keys():

	if wallet.public_key:
		response = {
			'public_key': wallet.public_key
		}

		return jsonify(response), 200

	else:
		response = {
			'message': 'Public Key not generated'
		}

		return jsonify(response), 404


@app.route('/transaction', methods=['POST'])
def add_transaction():
	request_data = request.get_json()

	if not request_data:
		response = {
			'message': 'Missing Transaction Data'
		}
		return jsonify(response), 400

	required_fields = ['recipient', 'amount']

	if not all(field in request_data for field in required_fields):
		response = {
			'message': 'Missing Transaction Data'
		}
		return jsonify(response), 400

	recipient = request_data['recipient']
	amount = request_data['amount']
	signature = wallet.sign_transaction(wallet.public_key, recipient, amount)
	success = blockchain.add_transaction(recipient, wallet.public_key, signature, amount)

	if success:
		response = {
			'message': 'Successfully Added Transaction',
			'transaction': {
				'sender': wallet.public_key,
				'recipient': recipient,
				'amount': amount,
				'signature': signature
			},
			'balance': blockchain.get_balance()
		}

		return jsonify(response), 201
	else:
		response = {
			'message': 'Transaction Failed'
		}

		return jsonify(response), 500


@app.route('/open_transactions', methods=['GET'])
def get_open_transactions():
	open_transactions = blockchain.get_open_transactions()

	dict_transactions = [tx.__dict__ for tx in open_transactions]

	return jsonify(dict_transactions), 200


@app.route('/balance', methods=['GET'])
def get_balance():

	balance = blockchain.get_balance()

	response = {
		'public_key' : wallet.public_key,
		'balance': balance
	}

	return jsonify(response), 200


def load_wallet():
	global blockchain, wallet

	wallet_loaded = wallet.load_keys()

	if wallet_loaded:
		print('[INFO] Wallet Loaded Successfully')
		blockchain = Blockchain(wallet.public_key)

	else:
		print('[INFO] Creating New Wallet')
		if wallet.create_keys():
			print('[INFO] Wallet Created Successfully')
			blockchain = Blockchain(wallet.public_key)

		else:
			print('[ERROR] Something Went Wrong.')
			exit()


if __name__ == '__main__':
	load_wallet()
	app.run(port=PORT)

