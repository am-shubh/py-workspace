from blockchain import Blockchain
from verification import Verification
from uuid import uuid4

class Node:

	def __init__(self):
		# self.id = str(uuid4())
		self.id = 'Shubh'
		self.blockchain = Blockchain(self.id)


	def get_transaction(self):
		tx_recipient = input("Enter Recipient's Name: ")
		tx_amount = float(input("Enter Transaction amount: "))

		return (tx_recipient, tx_amount)


	def listener(self):

		print('-'*30)
		print('Please Choose')
		print('1: Add a new transaction')
		print('2: Mine a new Block')
		print('3: Get Balance')
		print('4: Output blockchain')
		print('q: Quit')
		print('-'*30)

		while True:

			choice = input('\nYour Choice: ')

			# checking conditions
			if choice == '1':

				# getting transaction from user
				recipient, amount = self.get_transaction()

				if self.blockchain.add_transaction(recipient, self.id, amount=amount):
					print('[INFO] Transaction Added')
				else:
					print('[ERROR] Transaction Failed')

			elif choice == '2':
				self.blockchain.mine_block()
				print('[INFO] Block mined and added to blockchain')

			elif choice == '3':
				balance = self.blockchain.get_balance()
				print("[INFO] Balance: {:6.2f}".format(balance))

			elif choice == '4':
				print("[INFO] Blocks in Blockchain: \n",)
				for block in self.blockchain.get_chain():
					print(block)

			elif choice == 'q':
				break

			else:
				print('[ERROR] Invalid Input.. Enter Again')

			if not Verification.verify_chain(self.blockchain.get_chain()):
				print('Invalid Blockchain')
				break



node = Node()
node.listener()


