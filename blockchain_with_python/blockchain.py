import functools
from collections import OrderedDict
import json

from hash_util import hash_string_sha256, hash_block

# genesis or start block
genesis_block = {
	'previous_hash': '',
	'index': 0,
	'transactions': [],
	'proof': 100
}

# 10 coins rewarded to miners 
MINING_REWARD = 10

# initialising empty blockchain
blockchain = []

# list of transaction which are not mined yet 
open_transactions = []

# sender's address or Name
sender = 'Shubh'

participants = {'Shubh'}


def load_data():

	try:
		with open('blockchain.txt', mode='r') as f:
			global blockchain, open_transactions

			file_content = f.readlines()

			blockchain = json.loads(file_content[0][:-1])
			blockchain = [{
				'previous_hash': block['previous_hash'], 
				'index': block['index'], 
				'proof': block['proof'], 
				'transactions': [OrderedDict([
					('sender', tx['sender']),
					('recipient', tx['recipient']),
					('amount', tx['amount'])
				]) for tx in block['transactions']]
			} for block in blockchain]

			open_transactions = json.loads(file_content[1])
			open_transactions = [OrderedDict([
				('sender', tx['sender']),
				('recipient', tx['recipient']),
				('amount', tx['amount'])
			]) for tx in open_transactions]

	except IOError:
		print('[ERROR] Could not load Data')


def save_data():

	try:
		with open('blockchain.txt', mode='w') as f:
			f.write(json.dumps(blockchain))
			f.write('\n')
			f.write(json.dumps(open_transactions))

	except IOError:
		print('[ERROR] Could not save Data')


def get_balance(participant):

	if participant in participants:

		tx_sender = [[ tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
		
		open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
		tx_sender.append(open_tx_sender)

		amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

		tx_recipient = [[ tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

		amount_recieved = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

		return (amount_recieved - amount_sent)

	return None


# returns last block in blockchain
def get_last_block():
	return blockchain[-1]


def add_transaction(recipient: str, sender=sender, amount = 1.0):

	transaction = OrderedDict([
		('sender', sender),
		('recipient', recipient),
		('amount', amount)
	])

	if verify_transaction(transaction):
		open_transactions.append(transaction)
		participants.add(sender)
		participants.add(recipient)
		save_data()
		return True

	return False


# creates blockchain with genesis block
def create_genesis_block(genesis_block_value: list):
	blockchain.append(genesis_block_value)
	save_data()


# mines block
def mine_block():

	last_block = blockchain[-1]

	hashed_block = hash_block(last_block)

	proof = proof_of_work()

	reward_transaction = OrderedDict([
		('sender', 'MINING'),
		('recipient', sender),
		('amount', MINING_REWARD)
	])

	copied_transactions = open_transactions[:]
	copied_transactions.append(reward_transaction)
	
	block = {
		'previous_hash': hashed_block,
		'index': len(blockchain),
		'transactions': copied_transactions,
		'proof': proof
	}

	blockchain.append(block)
	return True


def verify_transaction(transaction):
	sender_balance = get_balance(transaction['sender'])
	return sender_balance >= transaction['amount']


def valid_proof(transactions, last_hash, proof):
	guess = (str(transactions) + str(last_hash) + str(proof)).encode()
	guess_hash = hash_string_sha256(guess)
	return guess_hash[0:2] == '00'


def proof_of_work():
	last_block = blockchain[-1]
	last_hash = hash_block(last_block)
	proof = 0
	while not valid_proof(open_transactions, last_hash, proof):
		proof += 1

	return proof


# comparing hash values
def verify_chain():

	for (index, block) in enumerate(blockchain):

		# genesis block
		if index == 0:
			continue

		if block['previous_hash'] != hash_block(blockchain[index - 1]):
			return False

		if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
			print('[ERROR] Proof of work is invalid')
			return False

	return True
	

def get_transaction():
	tx_recipient = input("Enter Recipient's Name: ")
	tx_amount = float(input("Enter Transaction amount: "))

	return (tx_recipient, tx_amount)


def initialize():

	try:
		with open('blockchain.txt', mode='r') as f:

			file_content = f.readlines()

			if not file_content:
				print('[INFO] Creating genesis block with value {}\n'.format(genesis_block))
				create_genesis_block(genesis_block)

			else:
				print('[INFO] initialising...')
				load_data()

	except IOError:
		print('[ERROR] File does not exixt')
		print('[INFO] Creating \'blockchain.txt\'')
		print('[INFO] Creating genesis block with value {}\n'.format(genesis_block))
		create_genesis_block(genesis_block)

	print('-'*30)
	print('Please Choose')
	print('1: Add a new transaction')
	print('2: Mine a new Block')
	print('3: Get Balance')
	print('4: Output blockchain')
	print('q: Quit')
	print('-'*30)

initialize()

while True:

	choice = input('\nYour Choice: ')

	# checking conditions
	if choice == '1':

		# getting transaction from user
		recipient, amount = get_transaction()

		if add_transaction(recipient, amount=amount):
			print('[INFO] Transaction Added')
		else:
			print('[ERROR] Transaction Failed')

	elif choice == '2':
		if mine_block():
			open_transactions = []
			save_data()

	elif choice == '3':
		name = input('Enter Participant\'s Name: ')
		balance = get_balance(name)

		if balance is None:
			print("[ERROR] Not Found... Invalid Name")
		else:
			print("[INFO] Balance of {}: {:6.2f}".format(name, balance))

	elif choice == '4':
		print("[INFO] Blocks in Blockchain : ", blockchain)

	elif choice == 'q':
		break

	else:
		print('[ERROR] Invalid Input.. Enter Again')

