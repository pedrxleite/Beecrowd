N, M = map(int, input().split())
P = list(map(int, input().split())) + [42195]
cont = 0
for i in range(N):
    if (P[i + 1] - P[i]) <= M:
        cont += 1
    else:
        print('N')
        break
    
if cont == N:
    print('S')