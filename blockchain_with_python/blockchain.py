# genesis or start block
genesis_block_value = [1]

# initialising empty blockchain
blockchain = []

# returns last block in blockchain
def get_last_block():
	return blockchain[-1]


# add transaction to blockchain and thus creates new block
def add_transaction(transaction_amount: float):
	last_block = get_last_block()
	blockchain.append([last_block, transaction_amount])


# creates blockchain with genesis block
def create_genesis_block(genesis_block_value: list):
	blockchain.append(genesis_block_value)


print('[INFO] initialising...')
print('[INFO] Creating genesis block with value {}\n'.format(genesis_block_value))
create_genesis_block(genesis_block_value)

print('-'*30)
print('Please Choose')
print('1: Add a new transaction value')
print('2: Output blockchain')
print('q: Quit')
print('-'*30)

while True:
	choice = input('\nYour Choice: ')

	# checking conditions
	if choice == '1':

		# getting transaction amount from user
		tx_amount = float(input("Enter Transaction amount: "))
		add_transaction(tx_amount)

	elif choice == '2':
		print("Blocks in Blockchain : ", blockchain)

	elif choice == 'q':
		break

	else:
		print('[ERROR] Invalid Input.. Enter Again')

