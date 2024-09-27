import os
os.system('cls')

def msg(nome):
    print(f'Olá {nome} sejá bem vindo!')
    name = 'Lucas'
    print(f'Dentro da função {name}')

nome = str(input('Qual seu nome? '))
msg(nome)
print(f'Fora da função {name}')   