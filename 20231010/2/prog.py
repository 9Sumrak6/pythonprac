from math import *

def scale(a, b, c, d, x):
    return (x-a) * (d - c) / (b - a) + c


W, H, a, b, f = input().split()

W, H, a, b = map(int, (W, H, a, b))
f = 'lambda x:' + f

screen = [[' '] * W for i in range(H)]
y_values = []


for i in range(W):
	y_values.append(eval(f)(scale(0, W-1, a, b, i)))

maxf, minf = max(y_values), min(y_values)

prevy = 0
for i in range(W):
    w=int(scale(minf, maxf, H - 1, 0, y_values[i]))

    screen[w][i] = "*"

    if i > 0:
    	left, right = min(prevy, w) + 1, max(prevy, w)
    	mid = (right - left ) // 2
    	
    	for j in range(left, right):
    		if j  <= mid:
    			screen[j][i - 1] = "*"
    		else:
    			screen[j][i] = "*"

    prevy = w

print("\n".join("".join(s) for s in screen))