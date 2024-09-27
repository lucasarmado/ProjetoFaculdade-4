import os
os.system ('cls')

filmes = ['Ford vs Ferrari','O Irlandês','JoJo Rabbit','Coringa','Adoráveis Mulheres','Historia de um Casamento','1917','Era uma vez em Hollywood']

print('Os três primeiros filmes da lista: ',filmes[:3])

print(f'O ultimo elemento é: {filmes[-1]}')

filmes.sort()

print('filmes em ordem alfabética: ',filmes)