n = int(input())
a, b, c = '-', '-', '-'

if n % 2 == 0 and n % 25 == 0:
    a = '+'
if n % 2 == 1 and n % 25 == 0:
    b = '+'
if n % 8 == 0:
    c = '+'
print('A', a, 'B', b, 'C', c)
