def avg(*params):
    return sum(params) / len(params)

inp = eval(input())
print(avg(*inp))
