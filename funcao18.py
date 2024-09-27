import os
os.system('cls')

def teste(a):
    if a > 0:
        return 'Positivo :)'
    else:
        return 'Negativo :('

numero = int(input('Digite um numero: '))

print(teste(numero))