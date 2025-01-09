N = int(input())
secoes = [int(x) for x in input().split()]
somat = sum(secoes)
somae = 0

for i in range(N):
    somad = somat - somae - secoes[i]
    somae += secoes[i]
    if somae == somad:
        print(i + 1)
        break
