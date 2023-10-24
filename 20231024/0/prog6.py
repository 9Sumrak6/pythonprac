import itertools

def repeater(seq, n):
    for i in seq:
        yield from itertools.repeat(i, n)

ite = iter(repeater([1, 2, 3], 2))
print([next(ite)])
print([next(ite)])
print([next(ite)])
print([next(ite)])
print([next(ite)])

