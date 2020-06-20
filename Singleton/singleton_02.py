



class Singleton:

	def __init__(self, *args, **kwargs):
		pass

	@classmethod
	def get_instance(cls, *args, **kwargs):
		# 利用反射，看着这个类有没有 _instance属性
		if not hasattr(Singleton, '_instance'):
			Singleton._instance = Singleton(*args, **kwargs)

		return Singleton._instance


s1 = Singleton() # 使用这种方式创建实例的时候，并不能保证单例
s2 = Singleton.get_instance()	# 只有使用这种方式创建的时候才可以实现单例
s3 = Singleton()
s4 = Singleton.get_instance()

print('id(s1):{}, id(s2):{}, id(s3):{}, id(s4):{}'.format(id(s1), id(s2), id(s3), id(s4)))


