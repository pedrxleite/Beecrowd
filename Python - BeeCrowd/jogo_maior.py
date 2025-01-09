N = int(input())

while N != 0:
    cont1 = 0
    cont2 = 0
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            cont1 += 1
        elif B > A:
            cont2 += 1
        else:
            pass
    print(f'{cont1} {cont2}')
    N = int(input())