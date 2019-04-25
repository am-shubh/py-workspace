import socket

port = 8888
HEADERSIZE = 10

try:
	cli_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
	print("socket creation failed with error %s" %(err))

cli_skt.connect((socket.gethostname(), port))

# connected to server for infinite time
while True:

	full_msg = ''
	new_msg = True

	# loops for each message recv and prints it
	while True:

		temp_msg = cli_skt.recv(16)

		if new_msg:
			# print(f"New message length:{temp_msg[:HEADERSIZE]}")
			msg_len = int(temp_msg[:HEADERSIZE])
			new_msg = False

		full_msg += temp_msg.decode("utf-8")

		if len(full_msg)-HEADERSIZE == msg_len:
			print(full_msg[HEADERSIZE:])
			new_msg = True
			full_msg = ''

