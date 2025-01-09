risada = input()
vogais = {'a', 'e', 'i', 'o', 'u'}
sovogal = [letra for letra in risada if letra in vogais]
if sovogal == sovogal[::-1]:
    print("S")  
else:
    print("N")  