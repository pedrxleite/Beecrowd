import time, string
esperado = input('Digite a frase que você deseja: ')
letras = string.ascii_lowercase + ' '
resultado = ''
for letra in esperado:
    for i in range(len(letras)):
        l = letras[i]
        print(resultado + l)

        if l == letra:
            resultado += l
            break
        time.sleep(0.01)
