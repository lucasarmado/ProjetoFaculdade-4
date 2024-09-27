import os
os.system('cls')

i = 1
maior = 0
menor = 0
media = 0

while (i <= 10):
    numero = int(input(f'Digite um inteiro {i}:  '))
    if i == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    media = media + numero
    i = i + 1

    
print(f'Maior: {maior} Menor: {menor} Media: {media/10}')            
      