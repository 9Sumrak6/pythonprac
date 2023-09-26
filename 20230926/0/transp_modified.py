from pprint import pprint

matr = list(list())
while a := input():
    matr.append(list(eval(a)))


n = len(matr)
if(all(len(i) == n for i in matr)):
    for i in range(n):
        for j in range(i + 1, n):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]


for i in matr:
    print(*i)
