from collections import defaultdict
N, M = map(int, input().split())
valores = defaultdict(int)
for i in range(1, N + 1):
    lista =  list(map(int, input().split())) 
    valores[i] = sum(lista)
certos = {indice: soma for indice, soma in sorted(valores.items(), key=lambda x: (x[1]))[:3]}
for k in certos:
    print(k)
