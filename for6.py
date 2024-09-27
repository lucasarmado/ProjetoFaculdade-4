import os
os.system('cls')

Maispesado = 0
Maisleve = 0
totalPesos = 0
mediaPesos = 0
qtd = 5

for c in range(0, qtd):
    peso = int(input('Digite os pesos: '))
    if c == 0:
        #primeiro elemento da leitura
        #ele sempre será o maior e o menor
        Maispesado = peso
        Maisleve = peso

    if peso > Maispesado:
        Maispesado = peso
    elif peso < Maisleve:
        Maisleve = peso

    totalPesos = totalPesos + peso

mediaPesos = totalPesos / qtd    

print(f'O mais pesado é {Maispesado} Kg')
print(f'O mais leve é {Maisleve} Kg') 
print(f'A media dos pesos é {mediaPesos}')
               