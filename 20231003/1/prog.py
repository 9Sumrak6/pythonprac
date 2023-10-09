def Pareto(*args):
    ans = []

    if not isinstance(args[0], tuple):
        ans.append((args[0], args[1]))
        return tuple(ans)

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