import os
os.system('cls')

numero1 = numero2 = 0
menu = 1

while menu !=0:
  print('CALCULADORA SIMPLES EM PYTHON')
  print('1. Soma')
  print('2. Subtração')
  print('3. Multiplicação')
  print('4. Divisão')
  menu = int(input('Digite a opção desejada: '))


  if menu > 0:
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))


  if (menu == 1):
    print(f'A soma é: {numero1+numero2}')
  elif (menu == 2):
    print(f'A diferença é: {numero1-numero2}')
  elif (menu == 3):
    print(f'A multiplicação é: {numero1*numero2}')
  elif (menu == 4):
    print(f'A divisão é: {numero1/numero2}')
  elif (menu == 0):
    print(f'Até breve')
  else:
    print(f'Opção invalida')
print('Fim de programa')                

   

 