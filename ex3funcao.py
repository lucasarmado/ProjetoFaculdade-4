import os
os.system('cls')


def teste(a):
    if a > 0:
        return 'Positivo :)'
    elif a == 0:
        return 'ZERO'
    else:
        return 'Negativo :('


numero = int(input('Digite um numero: '))

print(teste(numero))