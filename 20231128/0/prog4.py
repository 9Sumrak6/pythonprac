a = input().split()
b = a[1]
c = a[2]
a = a[0]

class A:
    f = a
class B:
    sec = b
class C:
    t = c

while s := input():
    match s.split():
        case [A.f, *args] if "yes" in args:
            print(1)
        case [B.sec]:
            print(2)
        case [C.t, *args, B.sec]:
            print(3)
        case _:
            print("Gay")
