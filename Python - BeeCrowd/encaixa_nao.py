N = int(input())
for i in range(N):
    A, B = list(map(str, input().split()))
    a = [int(x) for x in A]
    b = [int(digito) for digito in B]
    if a[-(len(b)):] == b:
        print('encaixa')
    else:
        print('nao encaixa')
