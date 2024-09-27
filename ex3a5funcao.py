import os
os.system('cls')

def serie(numero):
    s = 0
    for i in range(1,numero+1,1):
        s = s + (1/i)
    return s    


numero = int(input('Digite um numero: '))
print(f'O valor da série do numero {numero} é: {serie(numero)}')