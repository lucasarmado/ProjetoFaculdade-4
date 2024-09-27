import os
os.system('cls')


try:

    num = int(input('Entre com o numero: '))
    resto = (num % 2)

    if resto == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
except ValueError as erro:
    print(erro)
    print('Verificar o numero informado')            