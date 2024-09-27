import os
os.system('cls')

def msg(nome):
    print(f'Olá {nome}, seja bem vindo!')
    nome = 'Lucas'
    print(f'dentro da função {nome}')

nome = str(input('Qual seu nome: '))
msg(nome)
print(f'fora da função {nome}')    
