from math import *

def Calc(s, t, u):
	u = 'lambda x, y:' + u
	s = 'lambda x:' + s
	t = 'lambda x:' + t

	def h(x):
		return eval(u)(eval(s)(x), eval(t)(x))

	return h

print(cbrt(27))

print(Calc(*eval(input()))(eval(input())))