def travel(n):
    for i in range(n):
        yield "По кочкам"

    return "В яму"

def travelwrap(n):
    s = yield from travel(n)
    yield s


print(list(travelwrap(int(input()))))

