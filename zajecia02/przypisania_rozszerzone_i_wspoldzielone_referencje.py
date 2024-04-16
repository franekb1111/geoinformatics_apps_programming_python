#zad 13
K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(K,L,M,N)

#symbol += zadziałał inaczej niż konkatencja, += zmodyfikował także wartość N, do której przypisana była wcześniej wartość M, a konkatenacja tego nie zrobiła analogicznie dla L i K


