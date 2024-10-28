N = int(input('Informe a pressão desejada: '))
M = int(input('Informe a pressão lida: '))
while True:
    if M >= 0 and N >= 0 and M <= 40 and N <= 40:
        print(N - M)
        break
    else: 
        print('Valor não aceito, escolha um número entre 0 e 40.')
        N = int(input('Informe a pressão desejada: '))
        M = int(input('Informe a pressão lida: '))
