# Exercício 3:
# Criar uma lista que leia 5 números inteiros
# Apresente os valores lidos
# Apresente o maior valor
# Quantas vezes apareceu o número 4
# Pesquisar o método que pode fazer isso.
# Usar laço de repetição para contar.
# Em qual posição está o primeiro 2

lista = []
for i in range(5):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)

print('Os números digitados foram: ')
print(lista)
print('O maior valor é: ',max(lista))
print(f'O número 4 aparece {lista.count(4)} vezes')

#forma "raiz" de contar a ocorrência do número 4 nas listas
cont = 0
for i in lista:
    if i==4:
        cont = cont + 1
print(f'O número 4 aparece {cont} vezes')
print('o número 2 aparece na posição',lista.index(2))
