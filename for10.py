import os
os.system('cls')

cont     = 0
numero   = 0

numero = int(input('Digite um numero: '))

for x in range(1,10,1):
    fatorial = 1
    for cont in range (x, 1, -1):
        fatorial = fatorial * cont

    print(f'O fatorial de {x} é: {fatorial}')    