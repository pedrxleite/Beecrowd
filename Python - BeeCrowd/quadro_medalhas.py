from collections import defaultdict
N = int(input())
quadro = defaultdict(dict)
for _ in range(N):
    k, ouro, prata, bronze = map(str, input().split())
    quadro[k] = {'ouro': int(ouro),
                 'prata': int(prata),
                 'bronze': int(bronze)
                }
ordenado = sorted(
    quadro.items(),
    key = lambda x: (-x[1]['ouro'], -x[1]['prata'], -x[1]['bronze'], x[0])
)
for pais, medalhas in ordenado:
    print(f'{pais} {medalhas["ouro"]} {medalhas["prata"]} {medalhas["bronze"]}')