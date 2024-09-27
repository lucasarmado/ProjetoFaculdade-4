import os
os.system('cls')

i = 1
j = 1


while j <= 10:
    i = 1
    print('*************************************')
    print(f'Tabuada {j}/10')
    while i <= 10:
        print(f'{j} x {i} = {j*i}')
        i = i +1
    j = j + 1   

