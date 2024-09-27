import os
os.system('cls')

num = int(input('Entre com a tabuada desejada: '))


for i in range(1, 10+1):
     print(f'{i} x {num} = {i * num}')