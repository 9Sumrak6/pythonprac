import itertools
import sys


class C:
    def slide(self, seq, n):
        check, ite, cur = itertools.tee(seq, 3)
        
        for i in itertools.count(0):
            if len(list(itertools.islice(check, i, i + n))) == 0:
                return

            yield from itertools.islice(ite, i, i + n)

            check, ite, cur = itertools.tee(cur, 3)

exec(sys.stdin.read())