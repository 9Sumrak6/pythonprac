def Pareto(*args):
    if not isinstance(args[0], tuple):
        return args[0], args[1]

    ans = []
    for i in range(len(args)):
        fl = True
        for j in range(len(args)):
            if i == j:
                continue

            if args[j][0] >= args[i][0] and args[j][1] >= args[i][1] and (args[j][0] > args[i][0] or args[j][1] > args[i][1]):
                fl = False
                break

        if fl:
            ans.append(args[i])

    return tuple(ans)

print(Pareto(*eval(input())))