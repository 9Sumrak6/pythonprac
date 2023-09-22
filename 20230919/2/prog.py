last = 0
s = 0
while s <= 21:
    last = int(input())
    if last <= 0:
        print(last)
        break
    s += last
else:
    print(s)
