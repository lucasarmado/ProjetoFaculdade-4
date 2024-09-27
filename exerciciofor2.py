import os
os.system('cls')

equivalencia = 0
maior = 0
menor = 0

for i in range(10):
    valor = int(input('Entre com o valor: '))
    if i == 0:
        maior = valor
        menor = valor

    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

    equivalencia = equivalencia + valor


print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Total: {equivalencia}')                


   