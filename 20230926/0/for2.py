from pprint import pprint

matr = list(list())
while a := input():
    a = list(eval(a))
    matr.append(a)

n = len(matr)
for i in range(n):
    for j in range(i + 1, n):
        matr[i][j], matr[j][i] = matr[j][i], matr[i][j]


for i in range(n):
    for j in range(len(matr)):
        print(matr[i][j], end=' ')
    print()
