from math import *

funcs = {}

s_num = 0
while s := input():
    s_num += 1

    if s[0] == ':':
        f_name, *args, expr = s.split()
        funcs[f_name[1:]] = (expr, args)
    else:
        if len(s) >= 4 and s[:4] == 'quit':
            beg, end = -1, -1

            for i in range(4, len(s)):
                if beg < 0 and (s[i] == '"' or s[i] == "'") :
                    beg = i + 1
                elif end < 0 and (s[i] == '"' or s[i] == "'") :
                    end = i
                    break
                
            print(s[beg:end].format(len(funcs) + 1, s_num))
            break
        else:
            f_name = ''
            for i in range(len(s)):
                if s[i] == ' ':
                    f_name = s[:i]
                    break
            else:
                f_name = s

            if not funcs.get(f_name):
                continue

            params = dict()
            if len(funcs[f_name][1]) == 1:
                beg, end = -1, -1

                for i in range(len(f_name), len(s)):
                    if beg < 0 and (s[i] == '"' or s[i] == "'") :
                        beg = i + 1
                    elif end < 0 and (s[i] == '"' or s[i] == "'") :
                        end = i
                        break

                if beg < 0 or end < 0:
                    params = {f'{funcs[f_name][1][0]}' : eval(s.split()[1])}
                else:
                    params = {f'{funcs[f_name][1][0]}' : s[beg:end]}
            else:
                lst = s.split()[1:]
                for i in range(len(lst)):
                    lst[i] = eval(lst[i])

                params = dict(zip(funcs[f_name][1], lst))

            print(eval(funcs[f_name][0], globals() | params))
