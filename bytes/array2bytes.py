


def array2bytes(list):
	""" 数组转换成字节 """
	temp = bytes(list).hex()
	return bytes.fromhex(temp)
