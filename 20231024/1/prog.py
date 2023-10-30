import sys


def fib(self, m, n):
	a, b = 0, 1

	if m > n:
		return

	for i in range(m):
		a, b = b, a + b

	for i in range(n):
		yield b
		a, b = b, a + b

exec(sys.stdin.read())