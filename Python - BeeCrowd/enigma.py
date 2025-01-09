enigma = list(map(str, input().upper()))
crib = list(map(str, input().upper()))
cont = 0
cont2 = 0
partes = []

for i in range(len(enigma) - len(crib) + 1):
    partes = enigma[:(len(crib) + i)][i:]
    for j in range(len(crib)):
        if partes[j] != crib[j]:
            cont2 += 1
            if cont2 == len(crib):
                cont += 1
        else:
            break
    cont2 = 0
print(cont)
