import os
os.system('cls')

soma = 0

for i in range(1,11,1):
   if (i % 2) == 0:  
        soma = i + soma
        
print(f'A soma dos numeros pares entre 0 e 10 é de {soma}')