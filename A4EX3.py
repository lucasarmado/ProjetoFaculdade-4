import os
os.system('cls')

s1 = s2 = s3 = 0

while s1 != 1 or s2 != 0 or s3 != 1:
    s1 = int(input('Digite o valor do sensor 1: '))
    s2 = int(input('Digite o valor do sensor 2: '))
    s3 = int(input('Digite o valor do sensor 3: '))
    if s1 != 1 or s2 != 0 or s3 != 1:
        print('Sequencia Incorreta!')

print('Fim do programa')        