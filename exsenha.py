import os
os.system('cls')

usuarioInicial = '-'
senhaInicial = 'senha'
usuario = ''
senha = ''

while usuario != usuarioInicial and senha != senhaInicial:
    usuario = str(input('Digite seu usuário: '))
    senha = str(input('Digite sua senha: '))
    if usuario == usuarioInicial and senha == senhaInicial:
        print('Bem vindo ao sistema,',usuario)
    else:
        print('Usuário ou senha incorreta!')

print('Fim de programa!')        