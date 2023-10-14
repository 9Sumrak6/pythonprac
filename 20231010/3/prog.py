from math import *
from fractions import Fraction

s = input()
h, w = len(s) - 2, 0

dot_num = 0
tilda_num = 0

while s := input():
	fl = True
	
	for i in s:
		if i == '.' or i == '~':
			fl = False
			break
	if fl:
		break

	w += 1
	if s[1] == '.':
		dot_num += h
	elif s[1] == '~':
		tilda_num += h

s_dot = str(dot_num) + "/" + str(h * w)
s_tilda = str(tilda_num) + "/" + str(h * w)

water_num = ceil(tilda_num / w)

print('#' * (w + 2))
for i in range(h):
	if h > water_num + i:
		print('#', w * '.','#', sep='')
	else:
		print('#', w * '~','#', sep='')
print('#' * (w + 2))

if dot_num < tilda_num:
	t_num = 20
	d_num = round(20 * dot_num / tilda_num)
	l_max = len(str(tilda_num) + str(h * w)) + 1
else:
	d_num = 20
	t_num = round(20 * tilda_num / dot_num)
	l_max = len(str(dot_num) + str(h * w)) + 1

print(f'{d_num * "." :<20} {s_dot :>{l_max}}')
print(f'{t_num * "~" :<20} {s_tilda :>{l_max}}')