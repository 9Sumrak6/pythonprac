import itertools


def slide(seq, n):
    for i in itertools.count(0):
        check, ite = itertools.tee(seq, 2)

        if len(list(itertools.islice(check, i, i + n))) == 0:
            return

        yield from itertools.islice(ite, i, i + n)
