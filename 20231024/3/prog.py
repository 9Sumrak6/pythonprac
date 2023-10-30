import itertools

print(*sorted(set(filter(lambda x: x.count('TOR') == 2, ["".join(s) for s in itertools.product('TOR', repeat=abs(int(input())))]))))
