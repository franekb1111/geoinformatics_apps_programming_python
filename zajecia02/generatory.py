def generator():
    yield "poniedziałek"
    yield "wtorek"
    yield "środa"
    yield "czwartek"
    yield "piątek"
    yield "sobota"
    yield "niedziela"

x = generator()

for dzien in generator():
    print(dzien)

print()

print(next(x))
print(next(x))
print(next(x))


