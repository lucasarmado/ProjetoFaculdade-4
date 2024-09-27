import os
os.system('cls')




def media(tipo, nota1, nota2):
    media = 0
    if tipo == 'A':
        media = (nota1+nota2)/2
    elif tipo == 'P':
        media = (nota1*0.30) + (nota2*0.70)/(0.3 + 0.7)
    return media    

tipo = str(input('Entre com A para Aritmética ou P para Ponderada: ')) 
n1 = float(input('Entre com a nota 1: '))
n2 = float(input('Entre com a nota 2: '))

m = media(tipo, n1, n2)

print(f'A média final foi de {m}')     
