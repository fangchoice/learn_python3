



def singleton(cls):

	_instance = {}

	def _singleton(*args, **kwargs):
		if cls not in _instance:
			_instance[cls] = cls(*args, **kwargs)

		return _instance[cls]

	return _singleton

@singleton
class A:
	a = 1

	def __init__(self, x):
		self.x = x
		print('init method')

a1 = A(2)
a2 = A(3)
print('id(a1) : {}, id(a2) : {}'.format(id(a1), id(a2)))
print(a1, a2)
