class Num:
	def __get__(self, obj, name):
		try:
			a = getattr(obj, self.__name)
		except Exception:
			a = 0

		return a

	def __set__(self, obj, value):
		try:
			setattr(obj, self.__name, value.real)
		except Exception:
			setattr(obj, self.__name, len(value))

	def __set_name__(self, obj, name):
		self.__name = '_' + name

import sys
exec(sys.stdin.read())