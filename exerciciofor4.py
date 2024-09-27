import os
os.system ('cls')

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

for contador in range(inicio, fim, passo):
    print(contador)
print('fim')    