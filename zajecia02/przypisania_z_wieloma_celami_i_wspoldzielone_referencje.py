#zad 10
a = b = [1, 2, 3] 
b[0] = 'zmieniono'

#print(a)
#print(b)

#zmiana b wpłynęła również na a ponieważ przypisanie nastąpiło poprzez referncję
#lista jest mutowalna

#zad 11
c = a[:] #kopia listy
c[0] = 'nowa wartość'

print(c)
print(a)
print(b)

#referencja nie zadziałała w tym wypadku ponieważ zmiany dokonaliśmy na kopii listy a nie na niej bezpośrednio

#zad 12

x = y = 10

y += 1

print(x,y)

#zmiana y nie wpłynęła na x
#int mie jest mutowalny
