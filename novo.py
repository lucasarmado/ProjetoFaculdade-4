import os
os.system('cls')

a = int(input('Entre com o valor para A: '))
b = int(input('Entre com o valor para B: '))
c = int(input('Entre com o valor para C: '))

if (a > b) and (a > c):
  print('Maior A') 
  print('teste')
  if a >= 20:
      print(f'A vale {a}')

elif (b > a) and (b > c):
    print('Maior B')

else:
    print('Maior C')
 