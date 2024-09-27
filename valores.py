import os
os.system('cls')

a = int(input('Digite o numero 1: '))
b = int(input('Digite o numero 2: '))
c = int(input('Digite o numero 3: '))

if a < b and a < c:
    print('A é o menor dos três')
elif b < a and b < c:
    print('B é o menor dos três')
else:
    print(c,'é o menor dos três')