N = int(input())
va = 0
vb = 0
cartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
for i in range(N):
    va2 = 0
    vb2 = 0

    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    if cartas.index(a1) >= cartas.index(b1):
        va2 += 1
    else:
        vb2 += 1

    if cartas.index(a2) >= cartas.index(b2):
        va2 += 1
    else:
        vb2 += 1
    
    if cartas.index(a3) >= cartas.index(b3):
        va2 += 1
    else:
        vb2 += 1
    
    if va2 >= 2:
        va += 1
    elif vb2 >= 2:
        vb += 1

print(va, vb)