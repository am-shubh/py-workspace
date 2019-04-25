import socket
import time
from threading import Thread

PORT = 8888
connection_success_msg = '[INFO] Connection established with the server.'
HEADERSIZE = 10

try:
	skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
	print("socket creation failed with error %s" %(err))

skt.bind((socket.gethostname(), PORT))

# change arg to change number of connection to be handled by server
skt.listen(5)

# handles each conected client seperately, it sends the connection time every 2 seconds
def handle_client(clientsocket):

	startTime = time.time()

	while True:

		time.sleep(2)

		currentTime = time.time()

		# calculating the conenction time and sending it to client
		connectionTime = currentTime - startTime

		timeMsg = f"Connected since : {connectionTime} seconds"

		timeMsg = f'{len(timeMsg):<{HEADERSIZE}}' + timeMsg

		clientsocket.send(bytes(timeMsg, "utf-8"))


# server runs for infinite time and handles each client seperately using thread
while True:

	clientsocket, address = skt.accept()

	print(f"[INFO] connection established with {address}")

	# creating success message to send to each connected client
	connection_success_msg_with_header = f'{len(connection_success_msg):<{HEADERSIZE}}' + connection_success_msg

	# sending the initial connection success message
	clientsocket.send(bytes(connection_success_msg_with_header, "utf-8"))
	
	# passes the client socket to be handled seperately
	Thread(target=handle_client, args=(clientsocket,)).start()