T = int(input())
for i in range(T):
    p = 0
    n = int(input())
    ordem = []
    for i in range(n):
        comando = input()
        if comando == 'LEFT':
            p -= 1
            ordem.append(-1)
        elif comando == 'RIGHT':
            p += 1
            ordem.append(1)
        elif comando.startswith('SAME AS'):
            _, _, x = comando.split()
            x = int(x) - 1
            acao = ordem[x]
            p += acao
            ordem.append(acao)
    print(p)
