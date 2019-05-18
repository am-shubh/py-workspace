# genesis or start block
genesis_block = {
	'previous_hash': '',
	'index': 0,
	'transactions': []
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


def get_balance(participant):

	tx_sender = [[ tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
	
	open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
	tx_sender.append(open_tx_sender)

	amount_sent = 0
	for tx in tx_sender:
		if len(tx) > 0:
			for txns in tx:
				amount_sent = txns

	tx_recipient = [[ tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

	amount_recieved = 0
	for tx in tx_recipient:
		if len(tx) > 0:
			for txns in tx:
				amount_recieved += txns	

	return amount_recieved - amount_sent


# returns last block in blockchain
def get_last_block():
	return blockchain[-1]


def add_transaction(recipient: str, sender=sender, amount = 1.0):
	
	transaction = {
		'sender': sender,
		'recipient': recipient,
		'amount': amount
	}

	if verify_transaction(transaction):
		open_transactions.append(transaction)
		participants.add(sender)
		participants.add(recipient)
		return True

	return False


# creates blockchain with genesis block
def create_genesis_block(genesis_block_value: list):
	blockchain.append(genesis_block_value)


# hashing
def hash_block(block):
	return '-'.join([ str(block[key]) for key in block ])


# mines block
def mine_block():

	last_block = blockchain[-1]

	hashed_block = hash_block(last_block)

	reward_transaction = {
		'sender': 'MINING',
		'recipient': sender,
		'amount' : MINING_REWARD
	}

	copied_transactions = open_transactions[:]
	copied_transactions.append(reward_transaction)
	
	block = {
		'previous_hash': hashed_block,
		'index': len(blockchain),
		'transactions': copied_transactions
	} 

	blockchain.append(block)
	return True


def verify_transaction(transaction):
	sender_balance = get_balance(transaction['sender'])
	return sender_balance >= transaction['amount']


# comparing hash values
def verify_chain():

	for (index, block) in enumerate(blockchain):

		# genesis block
		if index == 0:
			continue

		if block['previous_hash'] != hash_block(blockchain[index - 1]):
			return False

	return True
	

def get_transaction():
	tx_recipient = input("Enter Recipient's Name: ")
	tx_amount = float(input("Enter Transaction amount: "))

	return (tx_recipient, tx_amount)


print('[INFO] initialising...')
print('[INFO] Creating genesis block with value {}\n'.format(genesis_block))
create_genesis_block(genesis_block)

print('-'*30)
print('Please Choose')
print('1: Add a new transaction')
print('2: Mine a new Block')
print('3: Output blockchain')
print('q: Quit')
print('-'*30)

while True:

	choice = input('\nYour Choice: ')

	# checking conditions
	if choice == '1':

		# getting transaction from user
		recipient, amount = get_transaction()

		if add_transaction(recipient, amount=amount):
			print('Transaction Added')
		else:
			print('Transaction Failed')

	elif choice == '2':
		if mine_block():
			open_transactions = []

	elif choice == '3':
		print("Blocks in Blockchain : ", blockchain)

	elif choice == 'q':
		break

	else:
		print('[ERROR] Invalid Input.. Enter Again')

