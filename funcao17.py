import os
os.system('cls')

#se caso a função ser chamada sozinha
#vai ser exibido apenas oque esta dentro dela.

def intervalo(ini=0, fim=10, passo=1):
    for item in range(ini, fim, passo):
        print(item)              

intervalo(fim=5, passo=1) #com inicio ou fim definido       