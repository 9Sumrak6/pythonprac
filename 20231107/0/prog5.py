def div_ab(a, b):
    try:
        return a / b
    except(ZeroDivisionError):
        return "inf"
    

lst = ((10,2),(1,0),(9,3))

for i in lst:
    print(div_ab(*i))
