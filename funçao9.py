import os
os.system('cls')

def contador(i,f,p):
    """
    Exibe uma contagem na tela
    :param i: inicio da contagem
    :param f: final da contagem
    :param e: passo de quanto
    :return: sem retorno
    Autor: Lucas
    Data: 30/09/2020
    """
    for c in range(i,f,p):  
        print(f'{c}',end = ' ')

help (contador)
contador(1,10, 2)        