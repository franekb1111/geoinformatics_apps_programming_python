# 15. Stwórz pusty słownik o nazwie ja.
# 16. Niech będzie to reprezentacja Twojej osoby, dodaj do niego klucze imie, nazwisko, wiek,
# rodzice (rodzice mają być reprezentowani przez listę z 2 zagnieżdżonymi słownikami o 2
# kluczach: imie i wiek.
# 17. Wypisz wartość klucza rodzice.
# 18. Wypisz jedynie imię pierwszego z rodziców.
# 19. Wypisz wszystkie klucze naszego słownika.
# 20. Sprawdź czy nasz słownik posiada klucz rodzenstwo, wypisz zmienną typu boolean.

ja = {}
ja = {"imie": "Franek", "nazwisko": "Batko", "wiek": 22, "rodzice": [{"imie": "Elzbieta", "wiek": 45}, {"imie": "Marek", "wiek": 44}]}

# print(ja["rodzice"])
# print(ja["rodzice"][0]['imie'])
# print(ja.keys())
# print("rodzenstwo" in ja.keys())

krotka1 =  (1,2,"3",4,2,5)
# print(f"Dlugosc: {len(krotka1)} Pierwszy wyraz: {krotka1[0]} \nWartosc 2 wystepuje {krotka1.count(2)} razy")

X = set("kalarepa")

Y = set("lepy")

print(X & Y)


