#zad 16
def zmien_wartosc(arg):
    if isinstance(arg, int):
        arg = 65482652
    elif isinstance(arg, list):
        arg[0] = 'kalafior'


arg = 2 #niemutowalne
zmien_wartosc(arg) 
print(arg) #2
arg = ['Kasia'] #mutowalne
zmien_wartosc(arg) 
print(arg) #['kalafior']

#zad 17
lista_podsumowan = []
def zamowienie_produktu(nazwa_produktu,*, cena, ilosc=1):
    podsumowanie = {'Nazwa': nazwa_produktu, 'cena_laczna': cena*ilosc, 'ilosc': ilosc}
    lista_podsumowan.append(podsumowanie)
    suma = 0
    for i in range(0, len(lista_podsumowan)):
        suma = suma + lista_podsumowan[i]['cena_laczna']
    return (lista_podsumowan, suma)


zamowienie_produktu("salata", cena=12)
zamowienie_produktu("koperek", cena=5, ilosc=3)
a = zamowienie_produktu("baklazan", cena=14, ilosc=5)

for el in lista_podsumowan:
    print(el)

print(f'Sumaryczna wartosc zamowienia: {a[1]}')


#zad 18
def stworz_raport(*args, **kwargs):
    for product_id in args:
        print(f"ID produktu: {product_id}")
        for key, value in kwargs.items():
            if key.startswith("z" + str(product_id) + "_"):
                string = "z" + str(product_id) + "_"
                print(f"{key[len(string):]}: {value}")
        print()

stworz_raport(101, 1032, z101_nazwa="Kubek termiczny", z101_cena="45.99 zł", z1032_nazwa="Długopis", z1032_cena="4.99 zł")





