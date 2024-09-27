import random
import os
os.system('cls')
resultado = str
nome = input('Digite seu nome: ')
print(10*'#')
print('1- PEDRA / 2- PAPEL / 3- TESOURA')
print(10*'#')
print(f'Bem vindo {nome}')

numero_pc = random.randint(1,3)
numero_jogador = int(input('Escolha um numero entre 1 e 3: '))
print(10*'#')
print(numero_pc)
print(numero_jogador)

if (numero_pc == 1) and (numero_jogador == 2):
    print(f'{nome} Ganhou')
elif (numero_pc == 1) and (numero_jogador == 3):
    print('Computador Ganhou')
elif (numero_pc == 1) and (numero_jogador == 1):
    print('EMPATE')
elif (numero_pc == 2) and (numero_jogador == 1):
    print('Computador Ganhou')
elif (numero_pc == 2) and (numero_jogador == 3):
    print(f'{nome} Ganhou')              
elif (numero_pc == 2) and (numero_jogador == 2):
    print('EMPATE')
elif (numero_pc == 3) and (numero_jogador == 1):
    print(f'{nome} Ganhou')
elif (numero_pc == 3) and (numero_jogador == 2):
    print('Computador Ganhou')    
elif (numero_pc == 3) and (numero_jogador == 3):
    print('EMPATE')
else:
    print('INVALIDO')            

   
            