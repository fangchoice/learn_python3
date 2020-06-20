

import threading
import time
import json

import requests

def show_time(func):

	def inner(*arg,**kwargs):
		start = time.time()
		values = func(*arg,**kwargs)
		end = time.time()
		print(values)
		print('共花费时间{}s'.format(end - start), '\n')		

	return inner

@show_time
def get_url_data(data):
	headers = {'Content-Type': 'application/json'}
	# url = 'http://39.107.106.130:8101/script'
	url = 'http://123.57.220.87/script'
	r = requests.post(url, data=data, headers=headers)
	return r.json()

def main():
	print('start...\n')

	data = []
	with open('600.txt', 'r') as f:
		data = f.read()
		# data = f.read().splitlines()


	threads = []
	for i in range(10):
		t = threading.Thread(target=get_url_data, args=(data,))
		threads.append(t)
		t.start()

	# values = get_url_data(data)
	# print(values)

if __name__ == '__main__':
	main()
  
  
  
