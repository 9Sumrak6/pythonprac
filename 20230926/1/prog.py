a, b = eval(input())
print(*[i for i in range(a, b) if i > 1 and all([i % e for e in range(2, int(i ** (1/2)) + 1)])])
