N, M = map(int, input().split())
lista = []
somas = []
for _ in range(N):
    entrada = list(map(int, input().split()))
    lista.append(entrada)
    somas.append(sum(entrada)) #soma linhas

for i in range(M): #soma colunas
    coluna = []
    for j in range(N):
        coluna.append(lista[j][i])
    somas.append(sum(coluna))
        
print(max(somas))
