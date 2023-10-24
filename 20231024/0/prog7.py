import itertools

print(*list(f"{e[0]}{e[1]}" for e in itertools.product('ABCDEFGH', '12345678')), sep='\n')
