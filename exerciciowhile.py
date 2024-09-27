import os
os.system('cls')

num = 0
tentativas = 1
while (num != 104):
    num = int(input("Digite um numero:"))

    if num >=0:
        print("Este numero é positivo ou zero")

    if num < 0:
        print('Este numero é negativo')

    tentativas = tentativas + 1

print(f'Parabens, vc acertou o numero {num} em {tentativas} tentativas')
print('Fim de programa')            