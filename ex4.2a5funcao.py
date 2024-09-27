import os 
os.system ('cls')

def verifica(num):
    soma = 0
    if num % 2 !=0:
        return False
    else:
        for i in range(1,num,1):
            if (num % i == 0):
                soma = soma + i
                if (soma == num):
                    return True
        return False            


num = int(input('Entre com o numero: '))
if (verifica(num)):
    print(f'o numero {num} é perfeito')
else:
    print(f'o numero {num} não é perfeito')    

                    