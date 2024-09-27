import os
os.system('cls')

v1 = float(input('Entre com o valor para V1: '))
v2 = float(input('Entre com o valor para V2: '))
op = input('+, -, *, /')

if op == '+':
  res = v1+v2
elif op == '-':
  res = v1-v2
elif op == '*':
  res = v1*v2
elif op == '/':
  if v2 != 0:
      res = v1/v2
  else:
        res = 'Divisão por Zero'
else:
    res = 'Operação Invalida'

print(res)          
