import os

a = ''
inp = input()
with open(inp, 'r') as f:
    for i in range(os.path.getsize(inp) // 3):
        a = f.read(1)
        print(a, end='')
    while a != '\n':
        a = f.read(1)
        print(a, end='')
