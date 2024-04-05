#zad 22
lista = [
    {'tytul': 'Ksiazka 1', 'autor': 'Zdzislaw', 'rok_wydania' : 1991}, 
    {'tytul': 'Ksiazka 2', 'autor': 'Marek', 'rok_wydania' : 2021}, 
    {'tytul': 'Ksiazka 3', 'autor': 'Adam', 'rok_wydania' : 2011}
]


posortowana_lista = sorted(lista, key=lambda x: x['rok_wydania']) 

print(posortowana_lista)

ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, lista))

print(ksiazki_po_2000)

tytuly_ksiazek = list(map(lambda x: x['tytul'], lista))

print(tytuly_ksiazek)

