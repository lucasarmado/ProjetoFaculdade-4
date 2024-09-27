import os
os.system('cls')

salario = int(input('Digite seu salário: '))

reajuste = salario * 0.25
salarioReajustado = salario + reajuste

print('Salário original era: ',salario)
print('Com o reajuste foi para: ',salarioReajustado)
