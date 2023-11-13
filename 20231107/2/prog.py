class InvalidInput(Exception):
	pass

class BadTriangle(Exception):
	pass

def triangleSquare(inp):
	try:
		(x1, y1), (x2, y2), (x3, y3) = eval(inp)
	except:
		print(0)
		raise InvalidInput

	print(1)

	try:
		x1, x2, x3 = float(x1), float(x2), float(x3)
		y1, y2, y3 = float(y1), float(y2), float(y3)

		ans = abs((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)) / 2

		tmp = 1 / ans

		return ans
	except:
		print(1)
		raise BadTriangle


ans = 0
fl = True
while fl:
	try:
		ans = triangleSquare(input())
		fl = False
	except InvalidInput:
		print("Invalid input")
	except BadTriangle:
		print("Not a triangle")
else:
	 print(f"{ans:.2f}")