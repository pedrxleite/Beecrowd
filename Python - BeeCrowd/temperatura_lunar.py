n = 1
while True: 
    N, M = map(int, input().split())
    if N == M == 0:
        break

    valores = [int(input()) for _ in range(N)]

    resultados = []
    soma = int(sum(valores[:M]))
    resultados.append(int(soma / M))

    for x in range(1, N - M + 1):
        soma = soma - valores[x - 1] + valores[x + M - 1]
        resultados.append(int(soma / M))
    
    print(f'Teste {n}\n{min(resultados)} {max(resultados)}\n')
    n += 1
