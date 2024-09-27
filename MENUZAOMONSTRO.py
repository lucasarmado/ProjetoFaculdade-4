import os
os.system('cls')

#definindo a função
def menu():
    print('------------------------------')
    print('    BEM VINDO AO SISTEMA      ')
    print('------------------------------')
    print('[1] cadastrar um cliente      ')
    print('[2] cadastrar um produto      ')
    print('[3] realizar uma venda        ')
    print('[4] imprimir o fluxo de caixa ')
    print('[0] sair do programa          ')

##passo a passo dos itens do menu *MANUALMENTE


#if opc == 1:
#    cliente = input('Digite o nome do cliente: ')
#    idade = input('Digite a idade: ')
#    print(f'Cliente registrado, {cliente}, {idade} anos.')
#elif opc == 2:
#       produto = input('Digite o nome do produto: ')
#       validade = input('Digite a validade: ')
#       print(f'Produto registrado, {produto}, válido até {validade}')
#elif opc == 3:
#       venda = input('Entre com o produto: ')
#    preco = input('Entre com o valor da venda: ')
#    descri = input('Dê uma breve descrição do produto: ')
#    print(f'Venda realizada: {venda}, com o preço inicial de {preco}. Descrição da venda: {descri}')
#elif opc == 4:
#    data = input('Digite a data desejada para impressão: ')
#    print(f'Imprimindo fluxo de caixa do dia {data}.....')
#elif opc == 0:
#    print('Fim do programa')

##AGORA UTILIZANDO FUNÇÃO


def op1():
    cliente = input('Digite o nome do cliente: ')
    idade = input('Digite a idade: ')
    print(f'Cliente registrado, {cliente}, {idade} anos.')

def op2():
    produto = input('Digite o nome do produto: ')
    validade = input('Digite a validade: ')
    print(f'Produto registrado, {produto}, válido até {validade}')

def op3():
    venda = input('Entre com o produto: ')
    preco = input('Entre com o valor da venda: ')
    descri = input('Dê uma breve descrição do produto: ')
    print(f'Venda realizada: {venda}, com o preço inicial de {preco}. Descrição da venda: {descri}')

def op4():
    data = input('Digite a data desejada para impressão: ')
    print(f'Imprimindo fluxo de caixa do dia {data}.....')


    

menu()
opc = int(input('Oque deseja fazer: '))



if opc == 1:
    op1()
elif opc == 2:
    op2()
elif opc == 3:
    op3()
elif opc == 4:
    op4()      
else:
    print('Fim do programa')




 
  


