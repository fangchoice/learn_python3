



import threading

class Singleton:

	_instance_lock = threading.Lock()

	# def __init__(self, *args, **kwargs):
	# 	pass

	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			with Singleton._instance_lock:
				if not hasattr(cls, '_instance'):
					Singleton._instance = super().__new__(cls, *args, **kwargs)

			return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)

def task(arg):
	obj = Singleton()
	print(obj)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()
  
