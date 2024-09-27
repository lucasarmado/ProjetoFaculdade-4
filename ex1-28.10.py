import os
os.system ('cls')
import random

numeros_extenso = ['zero','um','dois','tres','quatro','cinco']
numero_sorteado = random.randint(0,5)

print(f'Numero sorteado: {numero_sorteado} - {numeros_extenso[numero_sorteado]}')