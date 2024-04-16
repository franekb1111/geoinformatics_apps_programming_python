#zad 19
from math import pow

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return pow(podstawa, wykladnik)
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)


print(potega_2(4))

#zad 20

def licznik_a():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

licznik_1 = licznik_a()
print(licznik_1())
print(licznik_1())

global_count = 0

def licznik_b():
    global global_count
    global_count += 1
    return global_count

print(licznik_b())
print(licznik_b())

class Licznik:
    def __init__(self):
        self.count = 0
        
    def __call__(self):
        self.count += 1
        return self.count


licznik_2 = Licznik()

print(licznik_2())
print(licznik_2())

def licznik_d():
    if not hasattr(licznik_d, 'count'):
        licznik_d.count = 0
    licznik_d.count += 1
    return licznik_d.count

print(licznik_d())
print(licznik_d())


