import os
os.system('cls')

def parImpar(n1):
    if (n1 % 2 == 0):
        return 0
    else:
        return 1    




numero1 = int(input('Entre com um numero: '))

if parImpar(numero1)==0:
    print(f'O número {numero1} é par!')
else:
    print(f'O número {numero1} é impar')    