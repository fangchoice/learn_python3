


import socket
import sys
import time

import requests


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('192.168.1.121', 5612)

print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

try:
	with open('mac1.txt', 'r') as f:
		for line in f:
			mac = line.strip()
			url = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/259/value/0100"
			# url = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/261/value/C001FF?noresponse=1"
			# url = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/261/value/C20100?noresponse=1"
			# url = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/802/value/0100"
			response = requests.get(url)
			print(response.status_code)

			# url1 = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/261/value/A801FF"
			# url1 = "http://192.168.1.156/gatt/nodes/" + mac + "/handle/261/value/C20100?noresponse=1"
			# response1 = requests.get(url1)

			# 
			
			print('\nwaiting to receive message')
			data, address = sock.recvfrom(4096)

			print('received {} bytes from {}'.format(
        			len(data), address))

			print(bytes.hex(data))
			print('Mac: ',mac)
			battery = bytes.hex(data)
			print('battery: ', int(battery[-4:-2], base=16))

			# time.sleep(0.01)

			# 笔如果断开了有没有对应的接口获取到状态？
			# url2 = "http://192.168.1.156/management/nodes/connection-state?mac=&access_token="
			# response2 = requests.get(url2)	
			# print(response2.status_code)	
				

finally:
	print('closing socket')
	sock.close()		
