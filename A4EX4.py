import os
os.system('cls')

i = j = totalTabuadas = 0
totalTabuadas = int(input('Digite o total de tabuadas: '))

for j in range(1,totalTabuadas+1,1):
    print(f'Tabuada {j}/{totalTabuadas}')
    tabuada = int(input('Digite a tabuada desejada: '))
    limite = int(input('Digite até onde deseja: '))
    for i in range (1,limite+1,1):
        print(f'{tabuada} x {i} = {tabuada*i}')

print('Fim de programa!')

