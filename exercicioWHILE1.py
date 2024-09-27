contPares = contImpares = numero = 0

while numero >=0:
    numero=int(input('Digite um numero inteiro positivo, negativo para sair: '))
    
    if numero % 2 == 0:
        contPares = contPares + 1
    else:
        contImpares = contImpares + 1
print(f'Foram digitados:  {contPares} numeros pares e {contImpares} numeros ímpares ')            