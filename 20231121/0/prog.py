with open(input(), 'rb') as f:
    txt = f.read()

with open(input(), 'rw') as f:
    for i in range(f.seek(2) // 2):
        f.seek(i)
        a = f.read(1)
        f.seek(-i, 2)
        b = f.read(1)
        f.write(b)
        f.seek(-i, 2)
        f.write(a)


