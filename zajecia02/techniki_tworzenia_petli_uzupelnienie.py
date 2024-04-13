#zad 14

imiona = ['Anna', 'Jan', 'Ewa', "Zdzisław"]
oceny = [5, 4, 3]

for el in zip(imiona, oceny):
    print(el)

# w przypadku list o różnej długości przeiteruje do momentu gdy te listy mają tyle samo el
    
#zad 15
    
liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    y = x**2
    return y

lista_m = map(kwadrat, liczby)

print(*lista_m)

