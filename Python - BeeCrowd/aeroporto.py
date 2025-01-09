A, V = map(int, input().split())
n = 1
while True:
    if A == V == 0: 
        break

    voos = []
    for _ in range(V):
        X, Y = map(int, input().split())
        voos.append(X)
        voos.append(Y)

    quant = {}
    for voo in voos:
        quant[voo] = quant.get(voo, 0) + 1
    
    maior = max(quant.values())
    maiores = [str(indice) for indice, valor in quant.items() if valor == maior]
    maiores.sort()

    print(f'Teste {n}')
    print(f'{(" ".join(maiores))}', '')
    print()

    n += 1
    A, V = map(int, input().split())