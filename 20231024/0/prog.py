def fgen(n):
    s = 0
    for i in range(1, n + 1):
        yield (s := s + 1 / (i ** 2))

print(*list(fgen(int(input()))))

