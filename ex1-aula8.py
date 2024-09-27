import os
os.system ('cls')
#LEITURA DA FRASE
frase = str(input('Digite uma frase: '))
#EXIBIÇÃO DA FRASE
print('A frase digita foi',frase)
#TAMANHO DA FRASE  
tamanhoFrase = len(frase)
print(f'O tamanho da frase informada é: {tamanhoFrase}')

qtdEspacos = frase.count(' ')
print(f'A quantidade de espaços é: {qtdEspacos}')

qtdA = frase.count('a')
print(f'A quantidade de espaços é: {qtdA}')

fraseDividida = frase.split()
print('a segunda palavra é:',fraseDividida[1])

print(f'O tamanho da segunda palavra é: {len(fraseDividida[1])}')

