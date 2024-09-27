import os
os.system('cls')

numero = 0

while numero != 4 and numero != 9:
    numero=int(input('Digite um numero: '))
    if numero != 4 and numero != 9:
        print('Tente novamente!')
    
print('Fim do programa')

