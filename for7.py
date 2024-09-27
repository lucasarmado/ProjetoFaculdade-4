import os
os.system('cls')

x = 0
resposta = 's'

while resposta == 's':
        numero = int(input('Digite o numero: '))
        x = 0
        for contador in range (1 , numero+1):
            if (numero % contador == 0):
                #se entrar nesse if, é porque o numero é divisivel
                #por aquele do contador,que vai de 1 até o numero
                x = x + 1
        if (x > 2):
            print(f'O numero {numero} NÃO é primo')
        else:
            print(f'O numero {numero} é primo')
        resposta = str(input('Digite s para continuar: '))                        

print('fim')     



