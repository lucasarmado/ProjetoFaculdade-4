import os
os.system('cls')

def somatorio(numero):
    soma = 0
    for i in range(1, numero,1):
        soma = soma + i #acumulador
    return soma    




numero = int(input('Digite um numero: '))
print(f'O somatório de {numero} é {somatorio(numero)}')