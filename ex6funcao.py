import os
os.system('cls')



def calculadora(op, nota1, nota2):
    if op == '+':
        return (nota1 + nota2)
    elif op == '-':
        return (nota1 - nota2)
    elif op == '*':
        return (nota1 * nota2)
    elif op == '/':
        return (nota1 / nota2)       


n1 = float(input('Entre com o numero 1: '))
operaçao = input('Entre com a operação desejada: \n+ Adição \n- Subtração \n* Multiplicação \n/ Divisão\n') 
n2 = float(input('Entre com o numero 2: '))

resultado =calculadora(operaçao, n1, n2)
print(f'{n1} {operaçao} {n2} = {resultado} ')

