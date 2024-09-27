import os
os.system ('cls')


def fatorial(num):
    fat = 1
    for i in range(1,num+1,1):
        fat = fat * i
    return fat    


numero = int(input('Entre com um numero: '))        
print(f'O fatorial de {numero} é {fatorial(numero)}')