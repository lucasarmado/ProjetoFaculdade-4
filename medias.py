import os
os.system('cls')


nota1 = int(input('Digita a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1*0.40) + (nota2*0.60)/(0.4 + 0.6)

print(f'A sua média é: {media}')
    