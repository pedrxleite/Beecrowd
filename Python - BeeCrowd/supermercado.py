N = int(input())
valores = []

for _ in range(N):
    P, G = map(float, input().split())
    k = 1000 / G
    valores.append(P * k)

print(f'{min(valores):.2f}')