def sub(x, y):
	if isinstance(x, list) or isinstance(x, tuple):
		t = filter(lambda a: a not in y, x)
		return tuple(t) if isinstance(x, tuple) else list(t)
	else:
		return x - y

inp = eval(input())
print(sub(*inp))