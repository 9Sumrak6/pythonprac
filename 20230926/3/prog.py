matr1 = []
matr2 = []
res = []

matr1.append(list(eval(input())))
length = len(matr1[0])

i = 1
while inp := input():
	if i >= length:
		matr2.append(list(eval(inp)))
	else:
		matr1.append(list(eval(inp)))
		i += 1

for i in range(length):
	res.append([])
	for j in range(length):
		s = 0
		for k in range(length):
			s += matr1[i][k] * matr2[k][j]

		res[i].append(s)

for i in res:
	print(*i, sep=',')