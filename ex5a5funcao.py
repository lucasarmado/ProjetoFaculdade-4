import os
os.system ('cls')


def primo(num):
    soma = 0
    for i in range(1,num+1,1):
        if (num % i) == 0:
            soma += 1

    if soma == 2:
        return True
    else:
        return False

num = int(input('Entre com o numero: '))
if (primo(num)):
    print(f'o numero {num} é primo')
else:
    print(f'o numero {num} NÃO é primo')               
