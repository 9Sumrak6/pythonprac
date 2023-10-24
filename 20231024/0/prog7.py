import itertools

ite = itertools.product('ABCDEFGH', '12345678')

for i in range(64):
    print(*next(ite))
