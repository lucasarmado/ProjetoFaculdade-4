import os
os.system('cls')

salarioAtual = float(input('Digite seu salário atual: '))

if salarioAtual <= 3500:
    aumento = 1.1
else:
    aumento = 1.05

novoSalario = salarioAtual * aumento

print(f'O seu novo salário é: {round(novoSalario,2)}')
