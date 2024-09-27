import random


numeroPC = random.randint(0,10)
palpite = -1
tentativas = 1

while (palpite != numeroPC):
    palpite = int(input('Digite um numero: '))
    if (palpite != numeroPC):
        tentativas = tentativas + 1
    else:
        print('Errou tente novamente')
print(f'Parabéns, voce acertou o {palpite} e para isso precisou de {tentativas} tentativas')        
