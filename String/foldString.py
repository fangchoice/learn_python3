

string = "A1B2C3D4E5F6G7H8"

"""
字符串的长度为偶数，从中间分割成两部分fstpart, lastpart,
每两位为一整体，fstpart 与 lastpart相互对折

ex:对折之后的string为
  H8G7F6E5A1B2C3D4

"""

def fold_string(string):
	fst = []
	lst = []
	length = len(string)
	for i in range(1, length//2, 2):
		fst.append(string[i - 1] + string[i])
		lst.append(string[length - i - 1] + string[length - i])
	st = lst + fst
	str = "".join(i for i in st)
	return str

print('original string: {}'.format(string))
print('fold_string: {:>20}'.format(fold_string(string)))
