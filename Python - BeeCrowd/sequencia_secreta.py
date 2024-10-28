N = int(input())
valores = [int(input()) for _ in range(N)]
cont = 1

if valores[0] != 1 or valores[-1] != 1:
    valores.clear()
    valores = [int(input()) for _ in range(N)]

for i in range(len(valores) - 1):
    if valores[i] != valores[i + 1]:
        cont += 1

print(cont)