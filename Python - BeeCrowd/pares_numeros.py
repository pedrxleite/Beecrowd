N, I, F = map(int, input().split())

vetor = list(map(int, input().split()))

contador = 0

for i in range(N):
    for j in range(i + 1, N):
        soma = vetor[i] + vetor[j]

        if I <= soma <= F:
            contador += 1

print(contador)
