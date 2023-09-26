l, r = eval(input())
l = [i for i in range(l, r + 1) if i & 1]
print(*l)
