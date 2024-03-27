#zad 6
dane = (2024, 'Python', 3.8)

rok, jezyk, wersja = dane

print(f'{rok}, {jezyk}, {wersja}')

#zad 7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(f'{pierwsza}, {srodek}, {ostatnia}')

#zad 8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

imie, nazwisko, _, _, zawod = info

print(f'{imie}, {nazwisko}, {zawod}')

#zad 9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, [jezyk, wersja, opis] = dane

print(f'{rok}, {jezyk}, {wersja}, {opis}')

