lst = list(eval(input()))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if (lst[i] ** 2) % 100 > (lst[j] ** 2) % 100:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
