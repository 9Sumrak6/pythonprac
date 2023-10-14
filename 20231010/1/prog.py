from fractions import Fraction

def is_solution(s, w, *args):
	s, w = map(Fraction, (s, w))

	f1 = 'lambda x:'
	f2 = 'lambda x:'

	m = int(args[0])
	j = 1
	for i in range(m + 1):
		f1 += 'Fraction(str(x**' + str(m - i) + ')) * Fraction("' + args[j].strip() + '")'
		if i != m:
			f1 += ' + '
		j += 1

	n = int(args[j])
	j += 1
	for i in range(n + 1):
		f2 += 'Fraction(str(x**' + str(n - i) + ')) * Fraction("' + args[j].strip() + '")'
		if i != n:
			f2 += ' + '
		j += 1

	num = eval(f1)(s)
	denom = eval(f2)(s)

	if denom == 0:
		return False
	
	return num / denom == w

print(is_solution(*input().split(',')))