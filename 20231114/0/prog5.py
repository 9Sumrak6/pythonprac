class S:
    __slots__ = ["x"]

class R:
    pass

s = S()
r = R()
r.x = 100500
s.x = 100500
import sys
print(sys.getsizeof(s))
print(sys.getsizeof(r))
