import os
os.system('cls')

numero = soma = 0

while numero != -1:
   numero = int(input('Digite um numero: '))
   soma = soma + numero
print(f'A soma dos numeros digitados é: {soma}')   