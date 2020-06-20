



import time
import threading

class Singleton:

	_instance_lock = threading.Lock()

	def __init__(self, *args, **kwargs):
		time.sleep(1)

	@classmethod
	def get_instance(cls, *args, **kwargs):
		if not hasattr(Singleton, '_instance'):
			with Singleton._instance_lock:
				if not hasattr(Singleton, '_instance'):
					Singleton._instance = Singleton(*args, **kwargs)

		return Singleton._instance

def task(arg):
	obj = Singleton.get_instance(arg)
	print(obj)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()
  
