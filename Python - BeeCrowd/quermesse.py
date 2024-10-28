n = 1
while True:
    N = int(input())
    if N == 0:
        break
    nIngressos = [int(x) for x in input().split()]
    
    for i in range(N):
        if i + 1 == nIngressos[i]:
            print(f'Teste {n}\n{nIngressos[i]}\n')
            break
    n += 1
