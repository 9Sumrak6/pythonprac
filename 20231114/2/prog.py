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

from fractions import Fraction

class f(Fraction):
    fvalue = Num()

a, b = f(1, 2), f(7, 3)
a.fvalue = a + b
b.fvalue = list(a.fvalue for i in range(int(a.fvalue) + (b // 2)))
print(a.fvalue, b.fvalue)