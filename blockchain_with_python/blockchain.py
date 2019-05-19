import functools
import json

from utility.hash_util import hash_block
from block import Block
from transaction import Transaction
from utility.verification import Verification
from wallet import Wallet

# 10 coins rewarded to miners 
MINING_REWARD = 10

# participants = {'Shubh'}


class Blockchain:
	def __init__(self, hosting_node_id):

		# genesis or start block
		genesis_block = Block(0, '', [], 100, 0)

		# initialising empty blockchain
		self.__chain = [genesis_block]

		# list of transaction which are not mined yet 
		self.__open_transactions = []

		self.load_data()

		self.hosting_node = hosting_node_id


	def get_chain(self):
		return self.__chain[:]


	def get_open_transactions(self):
		return self.__open_transactions[:]


	def load_data(self):

		try:
			with open('blockchain.txt', mode='r') as f:

				file_content = f.readlines()

				blockchain = json.loads(file_content[0][:-1])

				updated_blockchain = []
				for block in blockchain:

					converted_tx = [Transaction(tx['sender'], 
											tx['recipient'],
											tx['signature'], 
											tx['amount']) 
									for tx in block['transactions']]

					updated_block = Block(block['index'], 
										block['previous_hash'],
										converted_tx,
										block['proof'],
										block['timestamp'])

					updated_blockchain.append(updated_block)

				self.__chain = updated_blockchain

				open_transactions = json.loads(file_content[1])

				updated_transactions = []
				for tx in open_transactions:
					updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount'])

					updated_transactions.append(updated_transaction)

				self.__open_transactions = updated_transactions

		except IOError:
			# print('[ERROR] Could not load Data')
			pass


	def save_data(self):

		try:
			with open('blockchain.txt', mode='w') as f:
				modified_blockchain = [block.__dict__ for block in [Block(block_element.index, 
																		block_element.previous_hash, 
																		[tx.__dict__ for tx in block_element.transactions],
																		block_element.proof,
																		block_element.timestamp ) for block_element in self.__chain]]
				modified_transaction = [tx.__dict__ for tx in self.__open_transactions]

				f.write(json.dumps(modified_blockchain))
				f.write('\n')
				f.write(json.dumps(modified_transaction))

		except IOError:
			print('[ERROR] Could not save Data')


	def get_balance(self):

		participant = self.hosting_node

		tx_sender = [[ tx.amount for tx in block.transactions if tx.sender == participant] for block in self.__chain]
			
		open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant]
		tx_sender.append(open_tx_sender)

		amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

		tx_recipient = [[ tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.__chain]

		amount_recieved = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

		return (amount_recieved - amount_sent)


	# returns last block in blockchain
	def get_last_block(self):
		return self.__chain[-1]


	def add_transaction(self, recipient: str, sender, signature, amount = 1.0):

		if self.hosting_node == None:
			return False

		transaction = Transaction(sender, recipient, signature, amount)

		if Verification.verify_transaction(transaction, self.get_balance):
			self.__open_transactions.append(transaction)
			self.save_data()
			return True

		return False


	# mines block
	def mine_block(self):

		if self.hosting_node == None:
			return None

		last_block = self.__chain[-1]

		hashed_block = hash_block(last_block)

		proof = self.proof_of_work()

		reward_transaction = Transaction('MINING', self.hosting_node, '', MINING_REWARD)

		copied_transactions = self.__open_transactions[:]

		for tx in copied_transactions:
			if not Wallet.verify_transaction(tx):
				print('[ERROR] transaction not verified')
				self.__open_transactions = []
				self.save_data()
				return None

		copied_transactions.append(reward_transaction)
		
		block = Block(len(self.__chain), hashed_block, copied_transactions, proof)

		self.__chain.append(block)
		self.__open_transactions = []
		self.save_data()
		return block


	def proof_of_work(self):
		last_block = self.__chain[-1]
		last_hash = hash_block(last_block)
		proof = 0

		while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
			proof += 1

		return proof

