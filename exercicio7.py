import os
os.system('cls')

qtdMetros = int(input('Digite uma qtd em metros: '))

qtdCm = qtdMetros * 100 
qtdMm = qtdMetros * 1000

print (f'{qtdMetros} metros equivalem a: {qtdCm} cm, e {qtdMm} mm')
