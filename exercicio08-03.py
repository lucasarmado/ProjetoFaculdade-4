import os
os.system('cls')

caixaPequena = 0
caixaMedia = 0
caixaGrande = 0

resposta = 's'

while resposta == 's':
    s1 = int(input("Digite para o sensor 1: "))
    s2 = int(input("Digite para o sensor 2: "))
    s3 = int(input("Digite para o sensor 3: "))

    if (s1 == 1 and s2 == 0 and s3 == 0):
        caixaPequena = caixaPequena + 1
        print("Caixa pequena!")
    elif (s1 == 1 and s2 == 1 and s3 == 0):
        caixaMedia = caixaMedia + 1
        print("Caixa Média!")
    elif (s1 == 1 and s2 == 1 and s3 == 1):
        caixaGrande = caixaGrande + 1
        print("Caixa Grande!")
    resposta = str(input('Deseja continuar (s/n)?'))        


print("###########################################")
print(f"Total de caixas pequenas: {caixaPequena}")
print(f"Total de caixas medias: {caixaMedia}")
print(f"Total de caixas grandes: {caixaGrande}")
