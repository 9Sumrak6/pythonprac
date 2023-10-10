from math import sin

def scale(a, b, c, d, x):
    return (x-a) * (d - c) / (b - a) + c

n = 30
c, d = -5, 5

for i in range(n):
    x = scale(0, n-1, -5, 5, i)
    y = sin(x)
    w=scale(-1, 1, 0, 20, y)
    print(int(w) * " ", "*")
