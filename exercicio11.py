BDuser = 'carlinhos'
BDpass = 'gabigostosa'

print('------------------------')
print('---------LOGIN----------')
print('------------------------')

usuario=input('Digite seu nome: ')


if usuario == BDuser:
    print('Olá',usuario)
    senha=input('Digite sua senha: ')
    if senha == BDpass:
        print('Seja bem vindo ao sistema!')
    else:
        print('Caro',usuario,'senha errada otario')
else:
    print('TUDO ERRADO PARÇA')            