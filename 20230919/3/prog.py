def dig_sum(n:int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        res = (n + i) * (n + j)
        print(n + i, '*', n + j, '=', end=' ')
        
        if dig_sum(res) == 6:
            print(':=)', end='')
        else:
            print(res, end='')
        if j == 2:
            print()
        else:
            print(end=' ')
        j += 1
    i += 1
