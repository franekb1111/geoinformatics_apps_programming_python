imiona = ['Marek', 'Arek', 'Kasia']

for imie in enumerate(imiona):
    print(imie)

liczba = int(input())

if (liczba > 0) & (liczba % 2 == 0):
    print(f"liczba {liczba} jest większa od 0 i parzysta")

if liczba != 0:
    print("Liczba jest różna od zera")

owoce = ["jabłko", "banan", "pomarńcza"]

owoc = input()

if owoc in owoce:
    print("owoc jest dostępny")

suma = 0

while (suma < 100):
    liczba2 = float(input())
    suma += liczba2

print(suma)
