import os
os.system('cls')

quadradolado = int(input('Tamanho dos lados do quadrado: '))
base = int(input('Base do quadrado: '))
altura = int(input('Altura do quadrado: '))

periQuadrado = (quadradolado*4)
areaQuadrado = (base*altura)

print(f'O perimetro do quadrado é {periQuadrado} e a área é {areaQuadrado}')

##########################################

baseRetangulo = int(input('Base do Retangulo: '))
alturaRetangulo = int(input('Altura do Retangulo: '))

periRetangulo = ((baseRetangulo*2)+(alturaRetangulo*2))
areaRetangulo = (baseRetangulo*alturaRetangulo)

print(f'O perimetro do retangulo é {periRetangulo} e a área é {areaRetangulo}')

##########################################
pi = 3.14
raioCirculo = int(input('Digite o raio do Circulo: '))
periCirculo = ((2*pi)*raioCirculo)
areaCirculo = (pi*(raioCirculo**2))

print(f'O perimetro do Circulo é {periCirculo} e a área é {areaCirculo}')

##########################################

ladoTriangulo = int(input('Entre com os lados do Triangulo: '))
baseTriangulo = int(input('Entre com a base do Triangulo: '))
alturaTriangulo = int(input('Entre com a altura do Triangulo: '))

periTriangulo = (ladoTriangulo*3)
areaTriangulo = ((baseTriangulo*alturaTriangulo)/2)

print(f'O perimetro do triangulo Equilatero é {periTriangulo} e a área é {areaTriangulo}')
