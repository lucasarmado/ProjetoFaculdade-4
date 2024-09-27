import os
os.system('cls')

ano = int(input('Digite o seu ano de nascimento: '))
anoAtual = int(input('Digite o ano atual: '))


if (anoAtual-ano) >= 18:
    print('voce ja pode tirar carta')
else:
    print('voce ainda nao pode tirar carta')    