import os
os.system('cls')

fatorial = 1
numero = int(input('Entre com um numero: '))
i = 1
while i <= numero:
    fatorial = fatorial * i
    i = i +1

print(fatorial)    