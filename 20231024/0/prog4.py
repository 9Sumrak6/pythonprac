import itertools

def fgen():
    s = 0
    for i in itertools.count(1):
        yield (s := s + 1 / (i ** 2))
ite = itertools.dropwhile(lambda x: x < 1.6, fgen())
print(*list(next(ite) for i in range(10)),sep = '\n')
