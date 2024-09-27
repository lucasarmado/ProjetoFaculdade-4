idade = 18
pi = 3.14
nome = 'LUCAS DAORINHA'

i, j = 24, 'Chaves'
print('resultado =', i, j)

a = 24
print(type(a))

a = 'HALLELUJAH'
print(type(a))

a = 1.57
print(type(a))

nome = 'Chaves'
mensagem = 'ninguem tem paciência comigo porra!'

print(nome, 'diz' ,mensagem)
print(nome + 'diz:' + mensagem)
print(nome + ' diz: ' + mensagem)

nome = 'Pedro '
sobrenome = 'Alvares Meupau'
nomeCompleto = nome + sobrenome
print('O Brasil foi descoberto por: '+nomeCompleto)

nome = 'Gulas'
casa = 8
print('O\npersonagem',nome,'\nmora na casa', casa)

nome = input('Olá, qual é o seu nome?')
print('Seja bem vindo', nome)

n1 = int(input('Digite o numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma de', n1,'e de',n2,'é',s)
print('A impressão COM Mascara versão 1')
print('A soma de {} e {} é igual a {}' .format(n1,n2,s))
print('A impressão COM Mascara versão 2')
print(f'A soma de {n1} e {n2} é igual a {s}')