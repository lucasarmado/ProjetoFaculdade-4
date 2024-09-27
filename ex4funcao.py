import os
os.system('cls')

x=0

def maior(a, b):
    if a > b:
        print(f'{a} é o maior')
    elif b > a:
        print(f'{b} é o maior')
    else:
        print(f'{a} e {b} são iguais')    

while (x != 666):
    x = int(input('digite dois numeros: '))
    y = int(input('digite dois numeros: '))
    maior(x,y)