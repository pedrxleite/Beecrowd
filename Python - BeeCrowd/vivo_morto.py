P = R = 1
n = 1
while True:
    P, R = map(int, input().split())
    if P == R == 0:
        break
    identificadores = list(map(int, input().split()))

    for _ in range(R):
        rodada = list(map(int, input().split()))
        nParticipantes, comando, jogadas = rodada[0], rodada[1], rodada[2:]
        identificadores = [identificadores[i] for i in range(nParticipantes) if jogadas[i] == comando]

    print(f'Teste {n}\n{identificadores[0]}\n')
    n += 1
