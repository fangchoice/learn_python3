

import json
import re

fe_store = []		# 将json文件全部以20个字节存放
join_store = []		# 将两个FE文件拼接成一个40个字节的list
store_count = []	# 存储count数
last_count = -1

with open('01126F5E5762.json', 'r') as f:
	data = json.load(f)

	for part in data:
		split_data = re.findall(r'.{20}', part)
		for i in split_data:
			fe_store.append(i)
		
for i in fe_store:
	cm = 0

	if i.startswith('FC'):
		fc_num = int(i[-2:], base=16)	# 取FC的后两位数字作为count
			

		if last_count != -1:
			if fc_num < last_count:
				cm = fc_num +247
			else:
				cm = fc_num
			if cm - last_count != 1:
				print('red')
		last_count = fc_num

		print('{:<40}, count = {}'.format( i, fc_num))

		store_count.append(fc_num)
	elif i.startswith('FE'):
		if i[3] == '1':
			join_store.append(i)
		if i[3] == '2':
			join_store.append(i)
			a = join_store[0] + join_store[1]				# 把两个FE拼接在一起
			fe_num = int(i[-10:-8], base=16)				# 取FE的两位数作为count
				

			store_count.append(fe_num)

			if last_count != -1:
				if fe_num < last_count:
					cm = fe_num + 247
				else:
					cm = fe_num 
				if cm - last_count != 1:
					print('red')
			last_count = fe_num
			print('{:<40}, count = {}'.format(a, fe_num))

			join_store.clear()

from itertools import groupby
# flag = -1
# store_count.append(198)
# store_count.append(200)

fun = lambda x: x[1] - x[0]
for k, g in groupby(enumerate(store_count), fun):
	l1 = [j for i, j in g] # 连续数字的列表
	if len(l1) > 1:
		scope = str(min(l1)) + '-' + str(max(l1))	# 将连续的数字范围用‘-’连接
	else:
		scope = l1[0]
	print('连续数字范围： {}'.format(scope))

