n = int(input())
valores = []

for i in range(n):
    valores.append(int(input()))

for numero in valores:
    if numero % 2 == 0 and numero > 0:
        print('EVEN POSITIVE')
    elif numero % 2 == 0 and numero < 0:
        print('EVEN NEGATIVE')
    elif numero % 2 == 1 and numero > 0:
        print('ODD POSITIVE')
    elif numero % 2 == 1 and numero < 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')