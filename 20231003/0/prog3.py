def recur(a):
    if a <= 0:
        return
    recur(a - 1)
recur(int(input()))
