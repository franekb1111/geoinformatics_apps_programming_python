# 2. Stwórz zmienną wartosc o wartości 100
# 3. Do zmiennej dodawanie przypisz wartość dodania do zmiennej wartosc liczby 123.15.
# 4. Stwórz zmienną potega i przypisz do niej zmienną dodawanie podniesioną do potęgi 12345.
# 5. Do zmiennej tekst przypisz rzutowanie wartości zmiennej potega na typ string.
# 6. Do zmiennej wartosc_pi przypisz wartość pi.
# 7. Do zmiennej losowa przypisz losową wartość z listy [1,2,3,4,5].

import math
import random
wartosc = 100

dodawanie = 100 + 123.15

potega = dodawanie**12

tekst = str(potega)

wartosc_pi = math.pi

losowa = random.choice([1,2,3,4,5])

# 8. Nadpisz zmienną tekst następującym wyrażeniem: tekst = f"Wartosc: {tekst}"
# 9. Wyświetl długość tekstu w zmiennej tekst i później wykorzystując wycinki wyświetl część
# zmiennej tekst o wartości „art”.
# 10. Wypisz wartość funkcji dir(tekst).
# 11. Zmień cały łańcuch znaków w zmiennej tekst na wielkie litery, wypisz.
# 12. Spróbuj zamienić znak na pozycji 2 w łańcuchu w zmiennej tekst na znak p



tekst = f"Wartosc: {tekst}"

# print(tekst)
# print(tekst[1:4])
# print(tekst.upper())
# print(dir(tekst))
#tekst[2] = 'p'
tekst = tekst.upper()

lista = list(tekst[:8])
lista.append([1,2,3,4,5])
print(lista)

lista2 = [1,2,3,"banan",100]

lista3 = [i**2 for i in lista2 if i != 'banan']

print(lista3)
lista4 = range(2,17,2)
lista4 = list(lista4)
print(lista4)
print(f"lista2:{lista2} lista3:{lista3} lista4:{lista4}")

