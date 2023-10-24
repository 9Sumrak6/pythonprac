import itertools

def f(n, seq):
    yield from itertools.filterfalse(lambda x: x%n, seq)
