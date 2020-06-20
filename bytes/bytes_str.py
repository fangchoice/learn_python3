

import socket

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# setblocking
# sock.setblocking(False)

# set option reused
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server_address
server_address = ('192.168.1.121', 5612)

# bind a address and port
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

 
def bytesToHexString(bs):
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X ' % b for b in bs])

while True:
	# wait for a connection
	print('waiting for a connection')
	# print('getpeername : {}'.format(sock.getpeername()))
	connection, client_address = sock.accept()

	# define three bytearray
	
	try:
		while True:
			data = bytes.hex(connection.recv(1024))		# 直接将bytes数据转换成str
			if not data:
				print('no data from: ', client_address)
				break
			# print(type(data))
			print('command received from:', len(data), client_address, data )
			# print('command received from:', client_address, data.decode('utf-8', 'ignore'))

	finally:
		# clean up the  connection
		connection.close()
    
    
