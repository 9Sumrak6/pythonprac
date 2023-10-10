from math import sin

def scale(a, b, c, d, x):
    return (x-a) * (d - c) / (b - a) + c

W, H = 60, 20
n = 30
c, d = -5, 5
lst=[[' '] * W for i in range(H)]
for i in range(W):
    x = scale(0, W-1, c, d, i)
    y = sin(x)
    w=int(scale(-1, 1, H - 1, 0, y))
    lst[w][i] = "*"

print("\n".join("".join(s) for s in lst))

