from decimal import Decimal

def esum(N, one):
    tp = type(one)
    s = tp(1)
    d = tp(1)
    t = tp(1) / d
    for i in range(N):
        s += tp(str(t))
        d += 1
        t /= d
    return s

print(esum(100, Decimal(1)))
