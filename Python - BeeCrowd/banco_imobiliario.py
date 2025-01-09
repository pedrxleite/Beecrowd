I, N = map(int, input().split())
D = E = F = I
for i in range(N):
    jogada = list(map(str, input().split()))
    dinheiro = int(jogada[-1])
    if len(jogada) == 3:
        if jogada[0] == 'C':
            if jogada.count('D') == 1:
                D -= dinheiro
            elif jogada.count('E') == 1:
                E -= dinheiro
            elif jogada.count('F') == 1:
                F -= dinheiro
        if jogada[0] == 'V':
            if jogada.count('D') == 1:
                D += dinheiro
            elif jogada.count('E') == 1:
                E += dinheiro
            elif jogada.count('F') == 1:
                F += dinheiro
    elif len(jogada) == 4:
        if jogada[1] == 'D':
            if jogada[2] == 'E':
                D += dinheiro
                E -= dinheiro
            elif jogada[2] == 'F':
                D += dinheiro
                F -= dinheiro
        elif jogada[1] == 'E':
            if jogada[2] == 'D':
                E += dinheiro
                D -= dinheiro
            elif jogada[2] == 'F':
                E += dinheiro
                F -= dinheiro
        elif jogada[1] == 'F':
            if jogada[2] == 'D':
                F += dinheiro
                D -= dinheiro
            elif jogada[2] == 'E':
                F += dinheiro
                E -= dinheiro
print(f'{D} {E} {F}')