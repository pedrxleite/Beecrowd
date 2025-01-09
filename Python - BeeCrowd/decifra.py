A, B, C, D = map(int, input().split())
multiplos = [n for n in range(1, C + 1) if C % n == 0]
for n in multiplos:
    if (n % A == 0) and (n % B != 0) and (D % n != 0):
        print(n)
        break