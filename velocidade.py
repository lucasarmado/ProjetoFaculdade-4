import os
os.system('cls')


velocidadeCarro = int(input('Digite a sua velocidade atual: '))
velRadar = int(input('Digite a velocidade permitida pelo radar: '))


media = velRadar * 1.1

if velocidadeCarro >= media:
  print('Reduza a velocidade da proxima vez, porque dessa vez voce vai pagar multa')
else:
    print('Não sera multado')  