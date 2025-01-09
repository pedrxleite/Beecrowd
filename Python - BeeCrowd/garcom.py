N = int(input())
cont = 0
for i in range(N):
    L, C = map(int, input().split())
    if L > C:
        cont += C
print(cont)